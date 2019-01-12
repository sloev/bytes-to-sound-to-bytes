
import sys
from PIL import Image

width = height = 64
data = [255] * 13
while True:
    ints = sys.stdin.buffer.read(1)
    if not ints:
        break
    data.append(ints[0])
    if len(data) % 64 == 0:
        data += [255] * 13
print(len(data))
data = data + ([0]*((width*height)-len(data)))
print(len(data))
data = bytes(data)

image = Image.frombytes("L", (width, height), data)
image.save('output.bmp')
