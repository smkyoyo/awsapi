#-*- coding: utf-8 -*-

import sys
import math
from konlpy.tag import Twitter
from konlpy.tag import Kkma
from konlpy.utils import pprint

## for twitter
tagger = Twitter()
## for kkma
#tagger = Kkma()
## for Mecab
#tagger = Mecab()

result = tagger.nouns('[품번6-2] 휴대폰 충전 케이블,USB케이블,마그네틱 케이블,자석 케이블,마그네틱 충전 케이블,휴대폰 젠더,충전기 젠더,안드로이드 젠더,아이폰 젠더,WSKEN')
#pprint(tagger.nouns('[품번6-2] 휴대폰 충전 케이블,USB케이블,마그네틱 케이블,자석 케이블,마그네틱 충전 케이블,휴대폰 젠더,충전기 젠더,안드로이드 젠더,아이폰 젠더,WSKEN'))
pprint(result)
print(type(result))
