import os
import sys
import random
import argparse

# @TODO Import your Ingestor and MemeEngine classes
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./_tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image filepy
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description="CLI for image path - body - author")
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--body', type=str, default=None)
    parser.add_argument('--author', type=str, default=None)
    
    args = parser.parse_args()
    path = str(args.path)
    body = args.body
    author = args.author
    
    print(f'{args.path} - {args.body} - {args.author}')
    print(generate_meme(path, body, author))