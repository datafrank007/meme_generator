import random
from ctypes import resize
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    def __init__(self, out_path: str):

        self.out_path = out_path

    def make_meme(self, img_path: str, body: str, author: str):
        img = Image.open(img_path, mode='r')
        meme_width = 500
        get_width = img.width
        out_path = self.out_path
        
        if get_width > meme_width:
            ratio = meme_width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((meme_width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        message = f'{body} - {author}'
        fontsize = 20
        font_path = './_data/Roboto/Roboto-Black.ttf'
        font = ImageFont.truetype(font_path, fontsize)
        draw.text((10, 400), message, font=font, fill = 'green')

        rand_digits = random.randint(0, 1000)
        meme_name = f'meme{rand_digits}.jpg'
        meme_path = f'{out_path}/{meme_name}'
        img.save(meme_path)
        return meme_path
    
    def __repr__(self):
        return f'<{self.body}, {self.author}>'

