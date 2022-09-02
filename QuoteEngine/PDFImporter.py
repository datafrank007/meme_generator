from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel

class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./_tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        quotes = []

        with open(tmp, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if len(line) > 3:
                    parsed = line.split(' - ')
                    new_quote = QuoteModel(parsed[0], parsed[1].strip())
                    quotes.append(new_quote)
                else:
                    continue

        file.close()
        os.remove(tmp)
        return quotes