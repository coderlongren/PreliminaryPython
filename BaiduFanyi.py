#coding=utf-8
import http.client
import hashlib
from urllib import parse
import random

appid = '20180227000128617'
secretKey = 'YUe_r7sK766rUpXcNPXU'
httpClient = None
myurl = '/api/trans/vip/translate'
q = 'love'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)
sign = appid+q+str(salt)+secretKey
m1 = hashlib.md5()
m1.update(sign.encode(encoding='utf-8'))
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

file = open(r'E:\result.txt' , 'w',encoding='UTF-8')
try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    response = httpClient.getresponse()
    str = response.read().decode('utf-8')
    str = eval(str)
    for line in str['trans_result']:
        file.write(line['dst']+'\n')
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
file.close()