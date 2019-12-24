#import PyInstaller
#PyInstaller -F webbrowser_test.py
from GH import Hello     #从包中导入
H=Hello                   #实例化
H.hello()                 #调用


