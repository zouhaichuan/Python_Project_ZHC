import webbrowser
webbrowser.open('http://www.sina.com/')#py文件名千万不能叫webbrowser，否则报错
import requests                         #也需要导入lib，很多
res=requests.get('http://tvapi.people.com.cn/rmsp/main/rmsp_main.xml')
type(res)
res.status_code == requests.codes.ok
res.raise_for_status()
playFile = open('RomeoAndJuliet.xml','wb') #保存xml文件
for chunk in res.iter_content(100000):
    playFile.write(chunk)
L=len(res.text)   #加入变量然后print
print(L)
print(res.text[:10000])

