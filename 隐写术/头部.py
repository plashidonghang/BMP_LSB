import sys

out_name = '3.bmp'
img = open('1.bmp','rb').read()
data = open('头部.txt','rb').read()
if len(data) > 4:
    exit()
f = open(out_name,'wb')
f.write(img[0:6])
f.write(data)  
f.write(img[6+len(data):])
f.close()
print ('Success!')


