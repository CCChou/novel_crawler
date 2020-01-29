import json
import logging.config


class Config:
    __store_dir = ''
    __logfile = ''

    @classmethod
    def init(cls, resource_dir):
        cls.__init_sys_config(resource_dir)
        cls.__init_logging_config(resource_dir)

    @classmethod
    def __init_sys_config(cls, resource_dir):
        with open(resource_dir + 'config.json') as file:
            cls.__store_dir = json.load(file).get('store_dir')

    @classmethod
    def __init_logging_config(cls, resource_dir):
        with open(resource_dir + 'logconf.json') as file:
            logging.config.dictConfig(json.load(file))

    @classmethod
    def store_dir(cls):
        return cls.__store_dir
