import time
import logging
from novel_crawler.config.config import Config
from novel_crawler.service.crawler_service import CrawlerService

if __name__ == '__main__':
    try:
        Config.init('../')
        logger = logging.getLogger(__name__)
        s = CrawlerService()
        begin = time.time()
        s.crawl('https://czbooks.net/n/cp167ak')
        end = time.time()
        logger.info(f'spend {end - begin}')
    except Exception as err:
        logger.error(err)
