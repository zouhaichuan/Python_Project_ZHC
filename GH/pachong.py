import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
buff = response.read()
html = buff.decode("utf8")
print(html)