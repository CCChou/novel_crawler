import re
from bs4 import BeautifulSoup
from novel_crawler.crawler.crawler import Crawler
from novel_crawler.crawler.utils.webutil import get_html
from novel_crawler.model.source import Source
from novel_crawler.model.document import Document
from novel_crawler.const.site import Site


class UUCrawler(Crawler):
    def get_name(self):
        html = get_html(self._url)
        html_page = BeautifulSoup(html, 'lxml')
        name = html_page.select_one('.jieshao_content > h1').get_text()
        return re.sub('最新章節', '', name)

    def get_links(self):
        html = get_html(self._url)
        html_page = BeautifulSoup(html, 'lxml')
        sources = []
        index = len(html_page.select('#chapterList a'))
        for a_tag in html_page.select('#chapterList a'):
            link = Site.UU.get_base().format(a_tag.get('href'))
            sources.append(Source(index, link))
            index -= 1
        return sources

    def get_document(self, source: Source):
        html = get_html(source.link)
        html_page = BeautifulSoup(html, 'lxml')
        title = html_page.select_one('#timu').get_text()
        content = html_page.select_one('#contentbox').get_text('\n', '<p>')
        clean_content = self.__get_clear_content(content)
        return Document(source.order, title, clean_content)

    def __get_clear_content(self, content):
        return re.sub(
            '[UＵwｗaａcｃhｈkｋmｍnｎoｏsｓuｕwｗ.．]{2}看书[\s]*[UＵwｗaａcｃhｈkｋmｍnｎoｏsｓuｕwｗ.．]+|\(adsbygoogle = window.adsbygoogle \|\| '
            '\[\]\).push\({}\);',
            '', content)
