#env 3.7
from PIL import Image,ImageFont
import textwrap
from pathlib import Path


def find_text_in_image(imgPath):
     image = Image.open(imgPath)
     red_band = image.split()[0]
     xSize = image.size[0]
     ySize = image.size[1]
     newImage = Image.new("RGB", image.size)
     imagePixels = newImage.load()
     for f in range(xSize):
         for j in range(ySize):
               if bin(red_band.getpixel((f, j)))[-1] == '0':
                        imagePixels[f, j] = (255, 255, 255)
               else:
                   imagePixels[f, j] = (0,0,0)
     newImgPath=str(Path(imgPath).parent.absolute())
     newImage.save(newImgPath+'/text.png')
     

find_text_in_image("clue.png")
find_text_in_image("clueTwo.jpg")
