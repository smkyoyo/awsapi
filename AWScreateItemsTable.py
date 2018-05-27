import boto3

dynamodb = boto3.resource('dynamodb')

### Create new table if not exists

table = dynamodb.create_table(
TableName = 'ItemsTable_Anal',
	KeySchema=[
		{
			'AttributeName':'productId',
			'KeyType':'HASH'
		},
		{
			'AttributeName':'categoryName',
			'KeyType':'RANGE'	
		},
	],
	AttributeDefinitions=[
		{
			'AttributeName':'productId',
			'AttributeType':'S'
		},
		{
			'AttributeName':'categoryName',
			'AttributeType':'S'
		},
	],
	ProvisionedThroughput={
		    'ReadCapacityUnits':5,
		    'WriteCapacityUnits':5
		}
)


table = dynamodb.Table('ItemsTable_Anal')
print(table.creation_date_time)

table.meta.client.get_waiter('table_exists').wait(TableName='ItemsTable')
print(table.item_count)


