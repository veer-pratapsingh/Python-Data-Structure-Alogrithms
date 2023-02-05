from PIL import Image
img = Image.open(r'projects\sample.jpg')
print(img.size)
img.show()