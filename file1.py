# -*- coding: UTF-8 -*-
import os
import sys

f=open('D:/test.txt','r')
with open('D:/test2.txt', "w", encoding="utf-8") as f2:   #只读打开文件
    f2.write('hehe')
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