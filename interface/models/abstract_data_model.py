from abc import ABCMeta
from typing import Dict


class AbstractDataModel(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def json() -> Dict:
        raise NotImplemented
