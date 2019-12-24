# -* - coding: UTF-8 -* -
 #import configparser
 import configparser
 import os

 os.chdir("D:\\")
 cf = configparser.ConfigParser()

  # read(filename) 读文件内容
filename = cf.read("CMC_MTG_MFS_S4320_2_CC_G0_1_MA5633.cfg")

print(filename)