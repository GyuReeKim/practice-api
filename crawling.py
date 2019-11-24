import requests
from bs4 import BeautifulSoup

genre_dict = {1: '드라마', 2: '판타지', 3: '서부', 4: '공포', 5: '로맨스', 6: '모험', 7: '스릴러', 8: '느와르', 9: '컬트', 10: '다큐멘터리', 11: '코미디', 12: '가족', 13: '미스터리', 14: '전쟁', 15: '애니메이션', 16: '범죄', 17: '뮤지컬', 18: 'SF', 19: '액션', 20: '무협', 21: '에로', 22: '서스펜스', 23: '서사', 24: '블랙코미디', 25: '실험', 26: '영화카툰', 27: '영화음악', 28: '영화패러디포스터'}

# 영화 주소 링크 필요
response = requests.get("https://movie.naver.com/movie/bi/mi/basic.nhn?code=136873").text
soup = BeautifulSoup(response, 'html.parser')

contents = soup.select('div.story_area > p.con_tx')
# print(contents)
audiences = soup.select('div.step9_cont > p.count')

genres = soup.select('dl.info_spec > dd:nth-child(2) > p')
temp_genres = genres[0].text.replace(',', '')
#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p

temp_genre_list = temp_genres.split()
# print(temp_genre_list)

genre = []
for key, val in genre_dict.items():
    for temp_genre in temp_genre_list:
        if temp_genre == val:
            genre.append(key)
            break
print(genre)


# audience = 0
# audience_str = ''
# for a in audiences:
#     for temp in a.text:
#         if temp == '명':
#             break
#         if temp != ',':
#             audience_str += temp
# audience = int(audience_str)
# print(audience)

# # 줄거리
# movie_info = []
# if len(contents) == 0:
#     movie_info.append("줄거리 없음")
# else:
#     for c in contents:
#         temp = c.text
#         temp = temp.replace('\r', '')
#         temp = temp.replace('\xa0', ' ')
#         temp = temp.replace('   ', ' ')
#         temp = temp.replace('  ', ' ')
#         movie_info.append(temp)
# print(movie_info)