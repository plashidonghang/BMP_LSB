from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os,sys


#字符串转化8位ASCII
def InfoToStr(data):
    str=''
    for i in range(0,len(data)):
        a = ''.join([bin(ord(c)).replace('0b', '') for c in data[i]])
        a = a.zfill(8)#向左添0，补全8位
        str=str+a
    return list(str)#返回一个字符数组

#打开图片获取像素值，并加密
def EnImg(information):
    k=0
    img = Image.open('1.bmp')
    width,height=img.size #获取图片的分辨率
    if width * height * 3 - 8 < len(information):
        print("加密信息过长！")
    else:
        img_array = img.load();
        #遍历图片每一个像素
        for i in range(0, height):
            for j in range(0,width):
                r,g,b=img_array[j,i]#获取该位置的RGB值
                R,k = BoolAndEncode(r, information, k)
                G,k = BoolAndEncode(g, information, k)
                B,k = BoolAndEncode(b, information, k)
                img_array[j,i]=(R,G,B)
        img.save('2.bmp')

#判断是否超出加密字符长度和对像素最低位进行修改
def BoolAndEncode(img_rgb,data,i):#像素，加密字符串，当前加密信息字符的位置
    img_rgb=dec2bin(img_rgb)#转为二进制
    if(i<len(data)):
        if(data[i]==0):#将像素最低位变为0
            img_rgb[7] = 0
        else:#将像素最低位变为1
            img_rgb[7] = 1
    if(i>=len(data) ):#and i<len(data)+8
        img_rgb[7] = 1
    img_rgb = bin2dec(img_rgb)#转为十进制
    i=i+1
    return img_rgb,i

#str数组转int数组
def StrToInt(info):
    info = [int(info) for info in info if info]
    return info

#十进制to二进制 
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

#主函数

#information = input("输入加密信息：")
information=open('数据.txt','rb').read().decode('gbk')
information = InfoToStr(information)
information = StrToInt(information)
#print(information)
EnImg(information)


