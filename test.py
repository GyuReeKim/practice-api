import urllib.request
import json
 
#애플리케이션 클라이언트 id 및 secret
client_id = "hG6O_G7PA_2DCtQbUri0" 
client_secret = "fsSh41QFYc"
 
#영화검색 url
url = "https://openapi.naver.com/v1/search/movie.json"
option = "&display=1"
query = "?query="+urllib.parse.quote('겨울왕국') # movieNm
url_query = url + query + option
 
#Open API 검색 요청 개체 설정
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
 
#검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    str_info = response_body.decode('utf-8')
    # print(type(temp))
    dict_info = json.loads(str_info)
    print(dict_info)
    # print(dict_info.get('items')[0].get('title').replace('<b>', '').replace('</b>', ''))
    print(dict_info.get('items')[0].get('link')) # 줄거리 크롤링에 필요
    # print(dict_info.get('items')[0].get('director'))

    # print(dict_info.get('items')[0].get('subtitle').replace('<b>', '').replace('</b>', ''))
    # print(dict_info.get('items')[0].get('userRating')) # string type
    print(dict_info.get('items')[0].get('image'))

else:
    print("Error code:"+rescode)