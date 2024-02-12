from novel_crawler.dao.epubfiledao import EpubFileDao
from novel_crawler.dao.kepubfiledao import KepubFileDao
from novel_crawler.dao.txtfiledao import TxtFileDao


class FileDaoProvider:
    @staticmethod
    def make_filedao(file_format: str, base_path):
        if file_format == 'txt':
            return TxtFileDao(base_path)
        elif file_format == 'epub':
            return EpubFileDao(base_path)
        elif file_format == 'kepub':
            return KepubFileDao(base_path)
        else:
            raise Exception("Unsupported format")