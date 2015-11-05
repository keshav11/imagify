from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (1080, 720), (255, 255, 255))
d = ImageDraw.Draw(img)
# text to imagify
i = raw_input()
d.text((30, 30), i, fill=(255, 0, 0))
img.save('test.png')
