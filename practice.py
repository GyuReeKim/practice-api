import requests
# from decouple import config
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
key = '660f73acbf0225280f5db341b9f4e840'
target = '20191121'
movie_url = f'{url}?key={key}&targetDt={target}'
res = requests.get(movie_url).json()
print(res)

daily = res.get('boxOfficeResult').get('dailyBoxOfficeList')
