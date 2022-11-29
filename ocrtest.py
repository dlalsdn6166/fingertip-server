import myocr
import myutil

path = 'sample.bmp'

print('try ocr..')

result = myocr.read(path)

print(result)

print('try encode..')

result = myutil.encode(result)

print(result)

print('done..!')