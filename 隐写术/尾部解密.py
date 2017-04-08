import sys
from PIL import Image

img = Image.open('4.bmp')
width, height = img.size  # 获取图片的分辨率

data=open('4.bmp','rb').read()
information = data[width*height*3+54:]
#print(information)
print(information.decode('gbk'))
