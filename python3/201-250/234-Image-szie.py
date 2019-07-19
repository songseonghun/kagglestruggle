from PIL import Image

image = Image.open('zalesia.png')
width, height = image.size

print(f'{width} x {height} pixels')

