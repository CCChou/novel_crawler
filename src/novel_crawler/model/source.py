class Source:
    def __init__(self, order, link):
        self.__order = order
        self.__link = link

    @property
    def order(self):
        return self.__order

    @property
    def link(self):
        return self.__link
