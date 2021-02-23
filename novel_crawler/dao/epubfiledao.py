import re
import os
from novel_crawler.model.document import Document
from ebooklib import epub


class EpubFileDao:
    def __init__(self, base_path):
        self.__base_path = base_path

    def save(self, document: Document):
        with open(self.__get_temp_file_path(document.order), 'w', encoding='utf8') as file:
            file.write(document.title)
            file.write('\n\n')
            file.write(document.content)
            file.write('\n\n')

    def __get_temp_file_path(self, index):
        return self.__base_path + str(index)

    def union(self, name, size):
        file_name = self.__get_valid_name(name)
        book = epub.EpubBook()
        book.set_identifier(file_name)
        book.set_title(file_name)
        book.set_language('zh')
        spine_list = ['nav']
        toc_list = []
        for index in range(1, size + 1):
            content = self.__read_content(index)
            lines_of_content = content.partition('\n')
            title = lines_of_content[0]
            ch = epub.EpubHtml(title=title, file_name='ch_{}.xhtml'.format(index), lang='zh')
            ch.content = '<h4>{}</h4>{}'.format(title, self.__create_content(lines_of_content[1:]))
            book.add_item(ch)
            spine_list.append(ch)
            toc_list.append(ch)

        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        style = 'BODY {color: white;}'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)
        book.toc = toc_list
        book.spine = spine_list
        epub.write_epub(self.__base_path + file_name + '.epub', book, {})

    def __get_valid_name(self, name):
        return re.sub('[:]', '', name)

    def __read_content(self, index):
        path = self.__get_temp_file_path(index)
        with open(path, 'r', encoding='utf8') as file:
            content = file.read()
        os.remove(path)
        return content

    def __create_content(self, lines):
        content = ''
        base = '<p>{}\n</p>'
        for line in lines:
            content += base.format(line)
        return content
