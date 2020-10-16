import sys
import time
import logging
from novel_crawler.config.config import Config
from novel_crawler.service.crawler_service import CrawlerService

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise Exception('Need the source url')

        Config.init('../')
        logger = logging.getLogger(__name__)
        s = CrawlerService()
        begin = time.time()
        s.crawl(sys.argv[1])
        end = time.time()
        logger.info(f'spend {end - begin}')
    except Exception as err:
        logger.error(err)
