import os
import sys
import urllib.request
import json

clientId = ""
clientSecret = ""
encText = urllib.parse.quote("\uacfc\uc790\\/\uac04\uc2dd")
url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=10&sort=count"

request = urllib.request.Request(url)
request.add_header("X-NAVER-Client-id", clientId)
request.add_header("X-NAVER-Client-Secret", clientSecret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
	response_body = response.read()
	print(response_body.decode('utf-8'))
else:
	print("Error Code:" + rescode)

''' 
jsonRt = response.read().decode('utf-8')
pyRt = json.loads(jsonRt)
'''
