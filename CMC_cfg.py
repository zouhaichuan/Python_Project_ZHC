# -* - coding: UTF-8 -* -
import os
import configparser


filepath = "D:\\test.ini"
conf = configparser.ConfigParser

#filezhc = conf.read("CMC_MTG_MFS_S4320_2_CC_G0_1_MA5633.cfg")
#print(filezhc)
#node ="mysql"

#key = "IP"

#value = "127.0.0.2"

#conf.set(node,key,value)

#fh = open(filepath ,'w')
fh = conf.read("test.ini")
#conf.write(fh)#把要修改的节点的内容写到文件中
print(fh)

#fh.close()

