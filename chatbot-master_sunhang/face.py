import requests
from decouple import config
import pprint

# 0. 이미지 파일
file_url = 'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/10556518_609155562538582_6550674291951338956_n.jpg?_nc_cat=104&_nc_oc=AQlZd6kc8gBIYSDZmCKeXkCSskyp2mbKRFx7k0N5yoVNuRoJjLNYzhf8Ice-zc7mP-g&_nc_ht=scontent-icn1-1.xx&oh=e706cc1581ed6649cdfc8dc3648e3b2f&oe=5DA89E1F'
response = requests.get(file_url, stream=True)
image = response.raw.read()
# 1. 네이버 API 설정
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
# 2. URL 설정
naver_url = 'https://openapi.naver.com/v1/vision/celebrity'
# 3. 요청보내기! POST
headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}

response = requests.post(naver_url, headers=headers, files={'image': image}).json()

best = response.get('faces')[0].get('celebrity')
pprint.pprint(best)
# if best.get('confidence') > 0.02:
#     text = f'{best.get('confidence')*100}%만큼 {best.get('value')}를 닮으셨네요.'
# else:
#     text = '사람 아닌듯...ㅠ'    
# print(text)
