import boto3
import os
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb=boto3.resource('dynamodb')

table = dynamodb.Table('ItemCategories')

#pe="CategoryName"
response = table.scan(
    FilterExpression=Attr('CategoryName')
    #ProjectionExpression=pe
)
'''
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):#pylint: disable=E0202
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)     
'''
for item in response['Items']:
    #print(json.dumps(item, cls=DecimalEncoder))
    #print(json.dumps(item))
    print(item['CategoryName'])
    #with open('ItemCategories.txt', 'w') as outfile:
    #    json.dump(item, outfile)


