import os
from novel_crawler.model.document import Document


class FileDao:
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
        with open(self.__base_path + name + '.txt', 'w', encoding='utf8') as file:
            for index in range(1, size + 1):
                file.write(self.__read_content(index))
                file.write('\n\n')

    def __read_content(self, index):
        path = self.__get_temp_file_path(index)
        with open(path, 'r', encoding='utf8') as file:
            content = file.read()
        os.remove(path)
        return content
