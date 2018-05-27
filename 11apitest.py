import requests

API_HOST = 'http://apis.skplanetx.com/11st'
headers = {'Authroization':'Bearer 684cbd3a29e8bdbdf80f7048061c5f26'}

def req(path, query, method, data={}):
	url = API_HOST + path
	print('HTTP Method: %s' % method)
	print('Request URL: %s' % url)
	print('Headers: %s' % headers)
	print('QueryString: %s' % query)

	if method == 'GET':
		return requests.get(url, headers=headers)
	else:
		return requests.post(url, headers=headers, data=data)

resp = req('/v2/common/categories?version={1}', '', 'GET')
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
print("response body:\n%s" % resp.text)
