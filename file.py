# -*- coding: UTF-8 -*-
import os
import sys

f=open('D:/test.txt','r')    #只读打开文件
while True:
   line = f.readline()
  # line = line.strip()
   line = line.rstrip().replace('邹可道','大可')
   if not line:
      continue
   else:
      failure = 0
      print(line)
f.close()


with open('D:/test1.txt','w') as f1: #with 写完了即关闭file了。
   f1.write('hello')
f1 = open('D:/test1.txt', 'r')
print(f1.read())








