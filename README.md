# Manipulating_Images
This Repository includes the python project where we are manipulating images using the PIL python image processing Library.

The objective of this projct is to modify image files that are available in the images.zip folder extract them and then perform image manipulating operations like resize (128,128), rotate(90) and update its file format to JPEG.

code for manipulation has been included in the modify_image.py file

input file has been take from images directory

output file has been kept to correct_images directory

steps for checking the correct output involves
1.python3
2.from PIL import Image
3.img = Image.open("ic_edit_location_black_48dp")
4.img.format, img.size

