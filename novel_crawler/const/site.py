from enum import Enum


class StrEnum(str, Enum):
    pass


class Site(StrEnum):
    UU = 'https://tw.uukanshu.com'

    def get_base(self):
        return self.value + '/{}'
