"""Abstract module for parsing quote inputs"""

from typing import List

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


class Ingestor(ImportInterface):
    importers = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
