from bs4 import BeautifulSoup
from novel_crawler.const.site import Site
from novel_crawler.crawler.crawler import Crawler
from novel_crawler.crawler.utils.webutil import get_html
from novel_crawler.model.source import Source
from novel_crawler.model.document import Document
from urllib.parse import urlparse
import re
from novel_crawler.crawler.utils.s2tutils import s2t


class X23qbCrawler(Crawler):
    def __init__(self, url):
        super().__init__(url)
        self.encoding = 'gbk'

    def get_name(self):
        html = get_html(self._url, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        name = html_page.select_one('.d_title > h1').get_text()
        return s2t(name)

    def get_links(self):
        html = get_html(self._url, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        sources = []
        index = 1
        for a_tag in html_page.select('.chaw_c > li > a'):
            link = Site.X23QB.get_base().format(a_tag.get('href'))
            sources.append(Source(index, link))
            index += 1
        return sources

    def get_document(self, source: Source):
        html = get_html(source.link, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        title = html_page.select_one('#mlfy_main_text > h1').get_text()
        content = self.__get_clean_content(html_page)
        content += self.__get_remaining_content(source.link, html_page)
        return Document(source.order, s2t(title), s2t(content))

    def __get_clean_content(self, html_page):
        for tag in html_page.select('#TextContent dt'):
            tag.decompose()
        for tag in html_page.select('#TextContent div'):
            tag.decompose()

        content = html_page.select_one('#TextContent').get_text('\n', '<p>')
        return re.sub('（继续下一页）|！！禁止转码、禁止阅读模式，部分内容隐藏，请退出浏览器阅读模式！|鉛筆小說 23qb.net', '', content)

    def __get_remaining_content(self, first_link, html_page) -> str:
        next_link = self.__get_next_link(html_page)
        if not self.__is_same_chapter(first_link, next_link):
            return ''

        link = Site.X23QB.get_base().format(next_link)
        html = get_html(link, self.encoding)
        html_page = BeautifulSoup(html, 'lxml')
        return self.__get_clean_content(html_page) + self.__get_remaining_content(first_link, html_page)

    def __get_next_link(self, html_page):
        scripts = html_page.select('script')
        last_script = scripts[len(scripts)-1]
        return re.search('(?<=nextpage=\")[^;]+(?=\";)', last_script.text).group(0)

    def __is_same_chapter(self, first_link, next_link):
        link_prefix = urlparse(first_link).path.split('.')[0]
        return next_link.startswith(link_prefix)
