from bs4 import BeautifulSoup
from novel_crawler.const.site import Site
from novel_crawler.crawler.crawler import Crawler
from novel_crawler.crawler.utils.webutil import get_html
from novel_crawler.model.source import Source
from novel_crawler.model.document import Document


class X23qbCrawler(Crawler):
    def __init__(self, url):
        super().__init__(url)
        self.encoding = 'gbk'

    def get_name(self):
        html = get_html(self._url, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        name = html_page.select_one('.d_title > h1').get_text()
        return name

    def get_links(self):
        html = get_html(self._url, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        sources = []
        index = 1
        for a_tag in html_page.select('#chapterList a'):
            link = Site.X23QB.get_base().format(a_tag.get('href'))
            sources.append(Source(index, link))
            index += 1
        return sources

    def get_document(self, source: Source):
        html = get_html(source.link, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        title = html_page.select_one('#mlfy_main_text > h1').get_text()
        content = self.__get_clean_content(html_page)
        return Document(source.order, title, content)

    def __get_clean_content(self, html_page):
        for tag in html_page.select('#TextContent dt'):
            tag.decompose()
        for tag in html_page.select('#TextContent div'):
            tag.decompose()
        return html_page.select_one('#TextContent').get_text()
