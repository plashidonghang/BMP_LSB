import sys

out_name = '4.bmp'
img = open('1.bmp','rb').read()
data = open('尾部.txt','rb').read()
f = open(out_name,'wb')
f.write(img[0:len(img)])
f.write(data)
#f.write(img[len(img):len(img)+len(data)])
f.close()
print ('Success!')


