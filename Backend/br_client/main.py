from rembg import remove
from PIL import Image

def removeImageBackgound(image):
    # print(str(image).split(".")[-2].split("/")[-1] + '-output.png')
    remove(Image.open(image)).save(('./test/' + str(image).split(".")[-2].split("/")[-1] + '-output.png'), 'PNG')

# removeImageBackgound('./test/test.jpg')