import decimal
import json
import math
import os
import sys
import boto3
from boto3.dynamodb.conditions import Attr, Key
from konlpy.tag import Kkma, Twitter
from konlpy.utils import pprint

readTableName = 'ItemsTable'
writeTableName = 'ItemsTable_Anal'

dynamodb = boto3.resource('dynamodb')
dynamodb2 = boto3.client('dynamodb')

paginator = dynamodb2.get_paginator('scan')
##############################################################
# Read existing table 'ItemsTable'
##############################################################
#ALL_ATTRIBUTES
iter = paginator.paginate(
    TableName = 'ItemsTable',
    Select = 'ALL_ATTRIBUTES',
    #FilterExpression = Attr('title')#.exists()
    PaginationConfig = {
        'MaxItem' : 1000000,
        'PageSize' : 1000
    }
)

##############################################################
# Write to existing table 'ItemsTable_Anal'
##############################################################
## for twitter
tagger = Twitter()
## for kkma
#tagger = Kkma()
## for Mecab
#tagger = Mecab()

#fw = open('ItemCategories2.txt', 'w')
table = dynamodb.Table(writeTableName)
pagenumber = 0
for page in iter:
    items = page['Items']
    pagenumber = pagenumber+1
    print('########################')
    print(pagenumber)
    print('########################')
    #print(type(items)) #list
    for item in items:
        #print(type(item)) #dict
        title = item['title']
        
        result = tagger.nouns(title['S'])
        categoryName = item['categoryName']
        link = item['link']
        image = item['image']
        lprice = item['lprice']
        hprice = item['hprice']
        mallName = item['mallName']
        productId = item['productId']
        productType = item['productType']
        
        
        with table.batch_writer(overwrite_by_pkeys=['productId']) as batch:
	        batch.put_item(
	            Item={
		            "categoryName": categoryName['S'],
		            "title": title['S'],
		            "link": link['S'],
		            "image": image['S'],
		            "lprice": lprice['S'],
		            "hprice": hprice['S'],
		            "mallName": mallName['S'],
		            "productId": productId['S'],
		            "productType": productType['S'],
                    "words": result
                }
            )
            
        print(title['S'])
        #break
        #fw.write(title['S'])
    

'''
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
'''

##############################################################
# CALL SPECIFIC_ATTRIBUTES
##############################################################
'''
iter = paginator.paginate(
    TableName = 'ItemsTable',
    AttributesToGet = ['title'],
    Select = 'SPECIFIC_ATTRIBUTES',
    #FilterExpression = Attr('title')#.exists()
    PaginationConfig = {
        'MaxItem' : 1000000,
        'PageSize' : 1000
    }
)
'''
##############################################################
# WRITE SPECIFIC_ATTRIBUTES
##############################################################
'''

for page in iter:
    items = page['Items']
    #count=0
    print(type(items)) #list
    for item in items:
        dic = item
        titles = dic['title']
        #print(type(titles)) #dictionary
        result = tagger.nouns(titles['S'])
        print(titles['S'])
        print(type(result))
        print(result)
       # pprint(result)
        #fw.write(titles['S']+'\n')
    break
'''
