from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (1080, 720), (255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Arial/ariali.ttf", 50)
# text to imagify
line = raw_input()
margin = 350
offset = 300
draw.text((margin, offset), line, font=font, fill=(0,0,0,255) )
img.save('test.png')
