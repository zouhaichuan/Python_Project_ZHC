# coding=utf-8
import configparser
 3 import os
 4
 5 os.chdir("E:\\Automation\\UI\\testcase")
 6 cf = configparser.ConfigParser()
 7
 8 # read(filename) 读文件内容
 9 filename = cf.read("test.ini")
10 print(filename)