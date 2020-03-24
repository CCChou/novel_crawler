import re
from bs4 import BeautifulSoup
from novel_crawler.crawler.crawler import Crawler
from novel_crawler.crawler.utils.webutil import get_html
from novel_crawler.model.source import Source
from novel_crawler.model.document import Document


class CZCrawler(Crawler):
    def get_name(self):
        html = get_html(self._url)
        html_page = BeautifulSoup(html, 'lxml')
        name = html_page.select_one('.title').get_text('', '[《》]')
        return re.sub('[《》]', '', name)

    def get_links(self):
        html = get_html(self._url)
        html_page = BeautifulSoup(html, 'lxml')
        sources = []
        index = 1
        for a_tag in html_page.select('.chapter-list a'):
            link = 'https:{}'.format(a_tag.get('href'))
            sources.append(Source(index, link))
            index += 1
        return sources

    def get_document(self, source: Source):
        html = get_html(source.link)
        html_page = BeautifulSoup(html, 'lxml')
        title = html_page.select_one('.name').get_text()
        content = html_page.select_one('.content').get_text()
        return Document(source.order, title, content)
