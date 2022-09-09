"""Imports quotes in txt format and converts to QuoteEngine objects"""

from typing import List

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel


class TXTImporter(ImportInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses input data and converts to quote objects"""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        file_ref = open(path, "r")
        lines = file_ref.readlines()
        for line in lines:
            parsed = line.split(' - ')
            new_quote = QuoteModel(parsed[0], parsed[1].strip())
            quotes.append(new_quote)

        file_ref.close()

        return quotes
