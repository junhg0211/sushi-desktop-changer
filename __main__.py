import ctypes
from datetime import date
from os.path import join, dirname

from PIL import Image, ImageFont, ImageDraw

FONT_PATH = './res/font/Inter-Bold.otf'

SHTELO_VANILLA = (253, 222, 89)
SHTELO_GRAY = (44, 44, 44)

WIDTH, HEIGHT = 3840, 2160

today = date.today()
target_date = date(today.year, 9, 1)
days = (today - target_date).days

if days < 0:
    days = f'D{days}'
elif days > 0:
    days = f'D+{days}'
else:
    days = 'D-DAY'

image = Image.new('RGB', (WIDTH, HEIGHT), SHTELO_GRAY)
draw = ImageDraw.Draw(image)

font = ImageFont.truetype(FONT_PATH, 512)

text_width, text_height = draw.textsize(days, font)

x = (WIDTH - text_width) / 2
y = (HEIGHT - text_height) / 2 - HEIGHT * 0.0382291667

draw.text((x, y), days, SHTELO_VANILLA, font=font)

image.save(filename := 'output.png')

path = join(dirname(__file__), filename)

ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

# os.remove(path)
