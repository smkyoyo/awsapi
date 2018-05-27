import boto3

dynamodb = boto3.resource('dynamodb')

'''
table = dynamodb.create_table(
		TableName = 'ItemCategories',
		KeySchema=[
			{
				'AttributeName':'CategoryName',
				'KeyType':'HASH'
			},
			{	
				'AttributeName':'CategoryCode',
				'KeyType':'RANGE'
			},
		],
		AttributeDefinitions=[
			{
				'AttributeName':'CategoryName',
				'AttributeType':'S'
			},
			{
				'AttributeName':'CategoryCode',
				'AttributeType':'N'
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits':5,
			'WriteCapacityUnits':5
		}
)
'''

table = dynamodb.Table('ItemCategories')
print(table.creation_date_time)


table.meta.client.get_waiter('table_exists').wait(TableName='ItemCategories')
print(table.item_count)


with table.batch_writer(overwrite_by_pkeys=['CategoryName', 'CategoryCode']) as batch:
    batch.put_item(
        Item={
            "CategoryName":"브랜드 여성의류",
            "CategoryCode":1001295,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001295.png"
        }
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 남성의류",
            "CategoryCode":1001296,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001296.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"브랜드 언더웨어",
            "CategoryCode":1001297,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001297.png"
        },
    )
    

    batch.put_item(
        Item={
            "CategoryName":"브랜드 여성신발",
            "CategoryCode":1001298,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001298.png"
        },
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 남성신발",
            "CategoryCode":1001299,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001299.png"
        },
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 여성가방",
            "CategoryCode":1001300,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001300.png"
        },
    )
    batch.put_item(
        Item={
            "CategoryName":"해외직구",
            "CategoryCode":1008286,
           "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_8286.png"
        },
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 남성가방",
            "CategoryCode":1001301,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001301.png"
        },
    )
    
    batch.put_item(
        Item={
            "CategoryName":"브랜드 여행가방",
            "CategoryCode":1001302,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001302.png"
        },
    )
    
    batch.put_item(
        Item={
            "CategoryName":"브랜드 지갑\/벨트",
            "CategoryCode":1001303,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001303.png"
       },
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 지갑\/벨트",
            "CategoryCode":1001303,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001303.png"
       },
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 쥬얼리",
            "CategoryCode":1001304,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001304.png"
       },
    )
    batch.put_item(
        Item={
            "CategoryName":"브랜드 시계",
            "CategoryCode":1001305,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001305.png"
       },
    )

    batch.put_item(
        Item={
            "CategoryName":"브랜드 잡화\/소품",
            "CategoryCode":1001306,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001306.png"
       },
    )    

    batch.put_item(
        Item={
            "CategoryName":"디자이너 여성의류",
            "CategoryCode":1001308,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001308.png"  
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"수입명품",
            "CategoryCode":1001307,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001307.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"디자이너 남성의류",
            "CategoryCode":1001309,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001309.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"디자이너 잡화",
            "CategoryCode":1001310,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001310.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"여성의류",
            "CategoryCode":1001311,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001311.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"언더웨어\/잠옷",
            "CategoryCode":1001313,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001313.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"남성의류",
            "CategoryCode":1001312,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001312.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"남성신발",
            "CategoryCode":1001315,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001315.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"여성신발",
            "CategoryCode":1001314,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001314.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"여성가방",
            "CategoryCode":1001316,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001316.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"남성가방",
            "CategoryCode":1001317,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001317.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"여행가방\/소품",
            "CategoryCode":1001318,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001318.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"시계",
            "CategoryCode":1001319,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001319.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"쥬얼리",
            "CategoryCode":1001320,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001320.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"패션잡화",
            "CategoryCode":1001322,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001322.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"지갑\/벨트",
            "CategoryCode":1001321,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001321.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"순금\/돌반지",
            "CategoryCode":1001323,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001323.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스킨케어",
            "CategoryCode":1001324,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001324.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"메이크업",
            "CategoryCode":1001325,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001325.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"선케어",
            "CategoryCode":1001326,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001326.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"남성화장품",
            "CategoryCode":1001327,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001327.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"향수",
            "CategoryCode":1001332,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001332.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"클렌징\/필링",
            "CategoryCode":1001328,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001328.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"헤어케어",
            "CategoryCode":1001329,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001329.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"바디케어",
            "CategoryCode":1001330,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001330.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"네일케어",
            "CategoryCode":1001331,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001331.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"뷰티소품",
            "CategoryCode":1001333,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001333.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"농산",
            "CategoryCode":1001334,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001334.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"수산",
            "CategoryCode":1001335,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001335.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"축산",
            "CategoryCode":1001336,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001336.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"반찬\/간편가정식",
            "CategoryCode":1001337,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001337.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"김치",
            "CategoryCode":1058375,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1058375.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"가공식품",
            "CategoryCode":1001338,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001338.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"커피\/생수\/음료",
            "CategoryCode":1001339,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001339.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"과자\/간식",
            "CategoryCode":1001340,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001340.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"즉석식품",
            "CategoryCode":1001341,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001341.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"건강식품",
            "CategoryCode":1001342,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001342.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"다이어트식품",
            "CategoryCode":1001343,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001343.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"기저귀",
            "CategoryCode":1001344,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001344.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"분유",
            "CategoryCode":1001345,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001345.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"물티슈",
            "CategoryCode":1001346,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001346.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"출산\/돌기념품",
            "CategoryCode":1001347,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001347.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"이유용품",
            "CategoryCode":1001348,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001348.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"도서\/음반",
            "CategoryCode":1002967,
           "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_2967.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"수유용품",
            "CategoryCode":1001349,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001349.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"e쿠폰\/상품권",
            "CategoryCode":1117025,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_117025.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아목욕\/스킨케어",
            "CategoryCode":1001350,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001350.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"여행\/숙박\/항공",
            "CategoryCode":1002878,
           "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_2878.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아세제\/위생용품",
            "CategoryCode":1001351,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001351.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아안전\/실내용품",
            "CategoryCode":1001352,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001352.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"외출용품",
            "CategoryCode":1001353,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001353.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"임부복\/소품",
            "CategoryCode":1001354,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001354.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"티켓\/공연",
            "CategoryCode":1865132,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_865132.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"신생아 의류",
            "CategoryCode":1001355,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001355.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아의류",
            "CategoryCode":1001356,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001356.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"아동\/주니어 의류",
            "CategoryCode":1001357,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001357.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아동신발",
            "CategoryCode":1001358,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001358.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"홈&카서비스",
            "CategoryCode":1001122,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001122.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아동잡화",
            "CategoryCode":1001359,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001359.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아가구\/침구",
            "CategoryCode":1001360,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001360.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아동식\/영양제",
            "CategoryCode":1001361,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001361.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"장난감",
            "CategoryCode":1001362,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001362.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"거실가구",
            "CategoryCode":1001363,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001363.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"침실가구",
            "CategoryCode":1001364,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001364.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"아웃도어가구",
            "CategoryCode":1001365,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001365.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"주방가구",
            "CategoryCode":1001366,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001366.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"수납가구",
            "CategoryCode":1001367,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001367.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"유아동가구",
            "CategoryCode":1001368,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001368.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"서재\/사무용가구",
            "CategoryCode":1001369,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001369.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"DIY자재\/용품",
            "CategoryCode":1001370,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001370.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"리모델링가구",
            "CategoryCode":1001371,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001371.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"침구",
            "CategoryCode":1001372,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001372.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"커튼\/블라인드",
            "CategoryCode":1001373,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001373.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"카페트\/러그",
            "CategoryCode":1001374,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001374.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"홈패브릭\/수예",
            "CategoryCode":1001375,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001375.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"조명",
            "CategoryCode":1001376,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001376.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"인테리어소품",
            "CategoryCode":1001377,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001377.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"구강\/세안\/면도",
            "CategoryCode":1001378,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001378.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"세탁용품",
            "CategoryCode":1001379,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001379.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"주방용품",
            "CategoryCode":1001380,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001380.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"욕실용품",
            "CategoryCode":1001381,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001381.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"청소용품",
            "CategoryCode":1001382,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001382.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"화장지",
            "CategoryCode":1001383,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001383.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"생리대\/성인기저귀",
            "CategoryCode":1001384,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001384.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"수납정리용품",
            "CategoryCode":1001385,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001385.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"세제\/방향\/살충",
            "CategoryCode":1001386,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001386.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"생활잡화",
            "CategoryCode":1001387,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001387.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"주방잡화",
            "CategoryCode":1058630,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1058630.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스포츠 의류",
            "CategoryCode":1001388,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001388.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스포츠 신발",
            "CategoryCode":1001389,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001389.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스포츠 잡화",
            "CategoryCode":1001390,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001390.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"등산\/아웃도어",
            "CategoryCode":1001391,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001391.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"골프",
            "CategoryCode":1001392,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001392.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"캠핑",
            "CategoryCode":1001393,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001393.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"낚시",
            "CategoryCode":1001394,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001394.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"자전거",
            "CategoryCode":1001395,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001395.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"헬스",
            "CategoryCode":1001396,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001396.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"요가\/필라테스",
            "CategoryCode":1001397,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001397.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스키\/보드",
            "CategoryCode":1001398,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001398.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"전동레저\/인라인\/킥보드",
            "CategoryCode":1001399,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001399.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"검도\/권투\/격투",
            "CategoryCode":1001400,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001400.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"구기스포츠",
            "CategoryCode":1001401,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001401.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"라켓스포츠",
            "CategoryCode":1001402,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001402.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"오토바이\/스쿠터",
            "CategoryCode":1001403,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001403.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"수영",
            "CategoryCode":1001404,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001404.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스킨스쿠버\/수상레저",
            "CategoryCode":1001405,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001405.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"기타 스포츠",
            "CategoryCode":1001406,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001406.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"안마용품",
            "CategoryCode":1001407,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001407.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"온열\/찜질용품",
            "CategoryCode":1001408,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001408.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"저주파\/적외선용품",
            "CategoryCode":1001409,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001409.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"건강관리용품",
            "CategoryCode":1001410,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001410.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"건강측정용품",
            "CategoryCode":1001411,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001411.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"당뇨관리용품",
            "CategoryCode":1001412,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001412.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"몸매관리용품",
            "CategoryCode":1001413,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001413.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"눈건강용품",
            "CategoryCode":1001414,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001414.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"손발건강용품",
            "CategoryCode":1001415,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001415.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"실버용품",
            "CategoryCode":1001416,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001416.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"재활운동용품",
            "CategoryCode":1001417,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001417.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"의약외품",
            "CategoryCode":1001418,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001418.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"병원\/의료용품",
            "CategoryCode":1001419,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001419.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"자동차용품",
            "CategoryCode":1001420,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001420.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"자동차기기",
            "CategoryCode":1001421,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001421.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"공구",
            "CategoryCode":1001422,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001422.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"전기\/산업자재",
            "CategoryCode":1001423,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001423.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"안전\/보안용품",
            "CategoryCode":1001424,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001424.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"스마트기기",
            "CategoryCode":1001425,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001425.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"카메라\/주변기기",
            "CategoryCode":1001426,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001426.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"게임",
            "CategoryCode":1001427,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001427.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"태블릿",
            "CategoryCode":1001428,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001428.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"휴대폰",
            "CategoryCode":1001429,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001429.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"TV",
            "CategoryCode":1001430,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001430.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"냉장고",
            "CategoryCode":1001431,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001431.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"세탁기",
            "CategoryCode":1001432,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001432.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"생활가전",
            "CategoryCode":1001433,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001433.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"주방가전",
            "CategoryCode":1001434,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001434.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"영상가전",
            "CategoryCode":1001435,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001435.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"음향가전",
            "CategoryCode":1001436,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001436.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"이미용가전",
            "CategoryCode":1001437,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001437.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"계절가전",
            "CategoryCode":1001438,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001438.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"노트북",
            "CategoryCode":1001439,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001439.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"데스크탑",
            "CategoryCode":1001440,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001440.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"모니터",
            "CategoryCode":1001441,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001441.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"프린터\/복합기",
            "CategoryCode":1001442,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001442.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"저장장치",
            "CategoryCode":1001443,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001443.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"PC부품",
            "CategoryCode":1001444,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001444.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"컴퓨터 주변기기",
            "CategoryCode":1001445,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001445.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"문구\/사무용품",
            "CategoryCode":1001446,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001446.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"화방용품",
            "CategoryCode":1001447,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001447.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"가전렌탈",
            "CategoryCode":1001448,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001448.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"꽃배달",
            "CategoryCode":1001449,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001449.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"꽃\/원예",
            "CategoryCode":1001450,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001450.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"악기",
            "CategoryCode":1001451,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001451.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"취미",
            "CategoryCode":1001452,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001452.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"애견용품",
            "CategoryCode":1001453,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001453.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"고양이용품",
            "CategoryCode":1001454,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001454.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"조류용품",
            "CategoryCode":1001455,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001455.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"관상어\/수족관",
            "CategoryCode":1001456,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001456.png"
        },
    )

    batch.put_item(
        Item={
            "CategoryName":"기타 동물용품",
            "CategoryCode":1001457,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1001457.png"
        },

    )
    batch.put_item(
        Item={
            "CategoryName":"비즈11번가",
            "CategoryCode":1059820,
            "CategoryImage":"http:\/\/m.11st.co.kr\/MW\/images\/categoryImage\/android\/cate_1059820.png"
            },    
    )      
