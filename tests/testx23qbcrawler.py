import unittest

from novel_crawler.crawler.x23qbcrawler import X23qbCrawler
from novel_crawler.model.source import Source


class X23qbCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.crawler = X23qbCrawler('https://www.x23qb.com/book/1041/')

    def test_get_name(self):
        print(self.crawler.get_name())

    def test_get_links(self):
        for source in self.crawler.get_links():
            print("order: {}, link: {}".format(source.order, source.link))

    def test_get_document(self):
        source = Source(1, 'https://www.x23qb.com//book/1041/224168.html')
        doc = self.crawler.get_document(source)
        print("title: {}\ncontent: {}".format(doc.title, doc.content))
