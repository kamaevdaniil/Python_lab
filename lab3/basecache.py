from abc import ABCMeta, abstractmethod


class BaseCache(metaclass=ABCMeta):

    @abstractmethod
    def clean(self, key):
        ...

    @abstractmethod
    def keep(self, key, value):
        ...

    @abstractmethod
    def refresh(self, key, value):
        ...

    @abstractmethod
    def check(self, key):
        ...