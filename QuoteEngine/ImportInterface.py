"""Generic interface for importing quote objects"""

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class ImportInterface(ABC):

    """
    ImporterInterface abstract class:
    This class implements a can_ingest class method which decides if a file
    is compatible with the importer.
    A parse abstract class method signature which we will realize and fully
    complete in the children classes that implement the ImporterInterface.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
