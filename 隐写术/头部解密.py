import sys

def Decode():
    img=open('3.bmp','rb').read()
    data=img[6:10]
    print(data.decode('gbk'))

Decode()