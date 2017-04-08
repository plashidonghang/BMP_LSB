import sys

def InfoToStr(data):
    str=''
    for i in range(0,len(data)):
        a = ''.join([bin(ord(c)).replace('0b', '') for c in data[i]])
        a = a.zfill(8)#向左添0，补全8位
        str=str+a
    return list(str)#返回一个字符数组

s1=open('a.txt','rb').read()
s1=s1.decode('gbk')
s1=InfoToStr(s1)
print(s1)
