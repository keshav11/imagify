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
    print length
    charactersInALine = 38
    r = length/charactersInALine + 1
    margin = 50
    offset = 50
    start = 0
    for i in range(0,r):
        end = charactersInALine*(i+1)
        for j in range(end,length):
            if line[end] == ' ':
                break;
            else:
                end = end + 1
        print start , ":" , end
        draw.text((margin, offset + 50*i), line[start:end], font=font, fill=(0,0,0,255))
        start = end

    img.save('test.png')

if __name__ == "__main__":
    imagify(sys.argv[1])
