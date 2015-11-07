import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def imagify(line):

    canvasL = 1080
    cavasH = 720
    img = Image.new('RGB', (canvasL, cavasH), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    size = 50
    font = ImageFont.truetype("Arial/ariali.ttf", size)
    length = len(line)
    charactersInALine = 38
    r = length/charactersInALine + 1
    margin = 50
    offset = 50
    for i in range(0,r):
        draw.text((margin, offset + 50*i), line[charactersInALine*i:charactersInALine*(i+1)], font=font, fill=(0,0,0,255))

    img.save('test.png')

if __name__ == "__main__":
    imagify(sys.argv[1])
