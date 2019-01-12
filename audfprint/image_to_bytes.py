from io import BytesIO
from PIL import Image
import sys
import numpy

size = 64
with BytesIO() as output:
    with Image.open(sys.argv[1]) as img:
        img = img.convert('L').crop()
        img.thumbnail((size, size))
        pixels = numpy.asarray(img)
        data = []
        for y in pixels:
            for pixel in y:
                data.append(pixel)
        data = bytes(data)
        sys.stdout.buffer.write(data)
