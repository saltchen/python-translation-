import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

'''
为了防止服务器识别出飞人类访问，需要修改head，对于修改head有两种方法，同时head对象是一个字典
通过add header()添加
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2950.5 Safari/537.36'

'''

data = {}
data['type'] = 'AUTO'
data['i' ]= content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2950.5 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])
