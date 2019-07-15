import pprint
import requests
from decouple import config

# 1. 토큰 및 기본 url설정
token = config('TELEGRAM_TOKEN') # .env 설정값 가져오기
base_url = f'https://api.telegram.org/bot{token}/'

# 2. getUpdates 정보 가져오기
response = requests.get(base_url+'getUpdates').json()
# print(response)

# 3. 나의 chat_id 가져오기 
# chat_id = []
# chat_id = response['result'][0]
# print(chat_id)

chat_id = response.get('result')[0].get('message').get('chat').get('id')
#chat_id = 796526229

# 4. chat_id에 메시지 보내기
# 4-1. 요청 보낼 url만들기
text = 'qwd'
api_url = f'{base_url}sendmessage?chat_id={chat_id}&text={text}'
# 4-2. requests로 보내기
requests.get(api_url)
