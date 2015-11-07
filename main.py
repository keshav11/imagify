import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def imagify(line):

    img = Image.new('RGB', (1080, 720), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial/ariali.ttf", 50)
    # text to imagify
    margin = 350
    offset = 300
    draw.text((margin, offset), line, font=font, fill=(0,0,0,255) )
    img.save('test.png')

if __name__ == "__main__":
    imagify(sys.argv[1])
