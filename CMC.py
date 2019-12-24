# -* - coding: UTF-8 -* -
 import configparser
 import os
 os.chdir("D:\\")
 cf = configparser.ConfigParser()
 # read(filename) 读文件内容
 filename = cf.read("test.ini")
 print(filename)