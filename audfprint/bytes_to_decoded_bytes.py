from reedsolo import RSCodec
import sys

rs = RSCodec(10)

data = []
while True:
    bytelist = sys.stdin.buffer.read(1)
    if not bytelist:
        break
    data.append(int(bytelist[0]))
data = bytes(data)
print(data)
decoded = rs.decode(data)
sys.stdout.buffer.write(decoded)