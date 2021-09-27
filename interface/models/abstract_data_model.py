from abc import ABCMeta, abstractmethod
from typing import Dict


class AbstractDataModel(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplemented
