import logging
from concurrent.futures import ThreadPoolExecutor
from novel_crawler.config.config import Config
from novel_crawler.crawler.crawler_provider import CrawlerProvider
from novel_crawler.dao.filedao_provider import FileDaoProvider


class CrawlerService:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    def crawl(self, url):
        self.__logger.info('init crawler')
        crawler = CrawlerProvider.create_crawler(url)
        name = crawler.get_name()
        sources = crawler.get_links()
        dao = FileDaoProvider.make_dao(Config.file_format, Config.store_dir())

        self.__logger.info('start crawling')
        with ThreadPoolExecutor(max_workers=8) as executor:
            for source in sources:
                executor.submit(self.__parse_and_save, crawler, source, dao)

        self.__logger.info('start union')
        dao.union(name, len(sources))

    def __parse_and_save(self, crawler, source, dao):
        logger = logging.getLogger(__name__)
        try:
            document = crawler.get_document(source)
            dao.save(document)
            self.__logger.info(document.title)
        except Exception as err:
            logger.error(err)
