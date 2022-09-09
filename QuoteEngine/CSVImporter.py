"""Imports quotes in CSV format and converts to QuoteEngine objects"""

from typing import List
import pandas

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel


class CSVImporter(ImportInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses input data and converts to quote objects"""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
