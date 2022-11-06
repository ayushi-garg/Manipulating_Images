#!/usr/bin/python3

from PIL import Image
import glob
for img in glob.glob('images/*'):
    im = Image.open(img)
    #print(str(img)[7:])
    im.rotate(90).resize((128,128)).convert('RGB').save("correct_images/"+str(img)[7:],'JPEG')
