## Shabak Challenge 2018 in Software and Data Science

To get into Challenges Web Page you need to find and enter password: `JOINUS`

Here is my video on how to find it:
https://youtu.be/BqK95ty95ao


## Challenge-1
Use Brute-Force for ZIP file
```
wget http://etgar.eastus.cloudapp.azure.com/software/clues.zip
sudo apt-get install fcrackzip 
fcrackzip -b -c 1 clues.zip        <-------here you get your password, Password is: 262626
unzip clues.zip﻿
```

Python Script need to be fixed:

[--------Start--------------]
```python
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
     
find_text_in_image("clue.png")﻿
```
[--------End-------------]

Decypt of file *clue.png* give image with text: 
#### Binary, Start 10,000 place, Fibonacci

This need to be used on Second Image *clueTwo.jpg*, no need to convert it.

10000buts / 8 = 1250 decimal place in file.

Use Binary Viewer on file *clueTwo.jpg* and start reading characters from Address 1250 by Fibonacci sequence.

Fibonacci Sequence: 1,2,3,5,8,13,21,34
```
1=y
2=o
3=u
5=g
8=o
13=t
21=i
34=t
```
`yougotit` add spaces and yo got secret answer `you got it`

<img src="Challenge1-Solution.png">

Here is my video on how to solve it:
https://youtu.be/m1NY8JyOT_0

