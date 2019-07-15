import requests
from decouple import config # 파이썬에서 환경변수 관리하는 패키지

# 1. 토큰 및 기본 url 설정
token = config('TELEGRAM_TOKEN') # .env 설정값 가져오기
base_url = f'https://api.telegram.org/bot{token}/'

# 2. getUpdates 정보 가져오기
response = requests.get(f'{base_url}getUpdates').json()
# print(response)

# 3. 나의 chat id 가져오기
# for i in response['result']:
#     print(i['message']['from']['id'])
# 836254550
chat_id = response['result'][0]['message']['from']['id']

# 4. chat_id에 메시지 보내기
# 4-1. 요청 보낼 URL 만들기
text = '인간시대의 끝이 도래했다!'
api_url = f'{base_url}sendMessage?chat_id={chat_id}&text={text}'
# 4-2. requests로 보내기
requests.get(api_url)