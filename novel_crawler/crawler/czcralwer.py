import requests
import re
from bs4 import BeautifulSoup
from novel_crawler.crawler.crawler import Crawler
from novel_crawler.model.source import Source
from novel_crawler.model.document import Document
from novel_crawler.const.site import Site


class CZCrawler(Crawler):
    def get_name(self):
        html = self.__get_html(self._url)
        html_page = BeautifulSoup(html, 'lxml')
        name = html_page.select_one('.title').get_text('', '[《》]')
        return re.sub('[《》]', '', name)

    def get_links(self):
        html = self.__get_html(self._url)
        html_page = BeautifulSoup(html, 'lxml')
        sources = []
        index = 1
        for a_tag in html_page.select('.chapter-list a'):
            link = 'https:{}'.format(a_tag.get('href'))
            sources.append(Source(index, link))
            index += 1
        return sources

    def __get_html(self, url):
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        req = session.get(url, headers=headers)
        return req.text

    def get_document(self, source: Source):
        html = self.__get_html(source.link)
        html_page = BeautifulSoup(html, 'lxml')
        title = html_page.select_one('.name').get_text()
        content = html_page.select_one('.content').get_text('\n', '<p>')
        return Document(source.order, title, content)
