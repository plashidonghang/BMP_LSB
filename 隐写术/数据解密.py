from PIL import  Image
import numpy as np
import matplotlib.pyplot as plt

def DeImg():
    s=''
    img = Image.open('数据.bmp')
    width,height=img.size #获取图片的宽，高
    img_array = img.load();
    #height = int(height/3)
    for i in range(0, height): #遍历图片每一个位置
        for j in range(0,width):
            r,g,b=img_array[j,i] #获取该位置的RGB值
            R = dec2bin(r)
            G = dec2bin(g)
            B = dec2bin(b)
            s=s+str(R[7])+str(G[7])+str(B[7])
        if "11111111" in s:#如果存在加密结束后留下的结束标志
            break
    return s

#十进制转二进制
def dec2bin(num):
    mid=[]
    while num != 0 :
        rem = num%2
        num = int(num/2)
        mid.insert(0,rem)
    for i in range(len(mid),8):
        mid.insert(0,0)
    return mid#返回一个二进制数组列表

#二进制to十进制
def bin2dec(num):
    s = ''
    for i in range(0, 8):
        s = s + str(num[i])
    a = int(s, 2)
    return a#返回一个整数

#ASCII码转字符，解密
def Decode(str_num):
    i=0
    code=''
    while(i+8<len(str_num)):
        s1=str_num[i:i+8]#截取第i位字符到i+8字符
        if(s1=='11111111'):#加密字符结束标志
            break
        i=i+8
        code=code+chr(bin2dec(s1))
    return code


#主函数
s=DeImg()
print("解密信息:")
print(Decode(s))