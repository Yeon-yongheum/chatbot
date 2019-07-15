import requests
from decouple import config

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
naver_url = ''
response = requests.post(naver_url).json