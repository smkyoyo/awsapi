import os
import sys
import urllib.request
import json
import boto3

'''
@Min Gyung Song
@2018.04.03
@Select all categories from DynamoDB
@Insert Naver shopping search results into DynamoDB
'''

## 항목 16501~16560개를 보는 중


class AWSConnector:
	
	### Connect to DynamoDB
	def connect_dynamo_db(self):
		dynamodb = boto3.resource('dynamodb')
		return dynamodb

	### Read existing table
	def read_existing_table(self, tableName, pe):
		dynamodb = self.connect_dynamo_db()
		try:
			table = dynamodb.Table(tableName)
			response = table.scan(
				ProjectionExpression = pe
			)
			items = response['Items']
			itemlists = []
			for item in items:
				itemlists.append(item['CategoryName'])
			return itemlists

		except table.meta.client.exception.ResourceInUseException:
			print('There is no table named' + tableName)
			sys.exit(1)

		
class NaverShoppingConnector: 
	
	def resultwriter(self, tableName, categoryName, title, link, image, lprice, hprice, mallName, productId, productType):
		aws = AWSConnector()
		dynamodb = aws.connect_dynamo_db()
		table = dynamodb.Table(tableName)
		with table.batch_writer(overwrite_by_pkeys=['productId']) as batch:
			batch.put_item(
				Item={
					"categoryName": categoryName,
					"title": title,
					"link": link,
					"image": image,
					"lprice": lprice,
					"hprice": hprice,
					"mallName": mallName,
					"productId": productId,
					"productType": productType
				}
			)
		print('succeeded')

	def naver_api_searcher(self, clientId, clientSecret, keyword, resultnumber, sortingmethod):
		
		keyword_final = keyword.replace("\\", "")
		encText = urllib.parse.quote(keyword_final)
		url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + resultnumber + "&sort=" + sortingmethod 
		request = urllib.request.Request(url)
		request.add_header("X-NAVER-Client-id", clientId)
		request.add_header("X-NAVER-Client-Secret", clientSecret)
		response = urllib.request.urlopen(request)
		rescode = response.getcode()
		#filename = "./" + keyword.replace("/", "") + "_response.txt"
		if(rescode==200):
			response_body = response.read()
			print(response_body.decode('utf-8'))
			result=json.loads(response_body.decode('utf-8'))
			subresult = str(result['items']).replace("\\","").replace("\'", "\"")#.replace("[", "").replace("]", "")
			#print(subresult)
			#subjsonresult=json.dumps(subresult)
			subjsonresult=json.loads(subresult)
			
			for i in range(0, len(subjsonresult)-1): 
				dict1 = subjsonresult[i]
				title = dict1['title']
				link = dict1['link']
				image = dict1['image']
				lprice = dict1['lprice']
				hprice = dict1['hprice']
				mallName = dict1['mallName']
				productId = dict1['productId']
				productType = dict1['productType']
				self.resultwriter('ItemsTable', keyword, title, link, image, lprice, hprice, mallName, productId, productType)
			
			#print(subjsonresult[0])
			#jsonfinalresult = json.loads(subjsonresult[0])
			#print(type(jsonfinalresult))

			#json.load()
			#f = open(filename, "a")
			#f.write(str(response_body.decode('utf-8')))
			#f.close()
			
		else:
			print("Error Code:" + rescode)
		#jsonRt = response.read().decode('utf-8')
		#pyRt = json.loads(jsonRt)

if __name__ == '__main__':

	clientId = ""
	clientSecret = ""
	sortingmethod = 'count'
	searchNumber = 100
	tableName = 'ItemCategories'
	pe = "CategoryName"

	### Connect to DynamoDB
	aws = AWSConnector()
	dynamodb = aws.connect_dynamo_db()

	## Read existing table
	items = aws.read_existing_table(tableName, pe)
	naver = NaverShoppingConnector()

	#naver.naver_api_searcher(clientId, clientSecret, items, str(searchNumber), sortingmethod)
	
	for item in items:
		naver.naver_api_searcher(clientId, clientSecret, item, str(searchNumber), sortingmethod)
	


