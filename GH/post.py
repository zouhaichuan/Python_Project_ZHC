import requests
import json
#url = 'http://official-account/app/messages/group'
#headers = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
#response = requests.post(url, data = json.dumps(body), headers = headers)
#print response.text
#print response.status_code
# POST是客户端提交数据（JSON、表格）给服务器端处理，如提交卡号，后端处理返回授权情况。
r = requests.get('http://tvapi.people.com.cn/rmsp/main/rmsp_main.xml')
#r.status_code
#r.headers['content-type']