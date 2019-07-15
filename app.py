import pprint
import random

from decouple import config
import requests
from flask import Flask, request

app = Flask(__name__)
token = config('TELEGRAM_TOKEN')
base_url = f'https://api.telegram.org/bot{token}'

@app.route(f'/{token}', methods=['POST'])
def telegram():
    response = request.get_json()
    # 만약에 메시지가 있으면
    if response.get('message'):
        # 사용자가 보낸 메시지를 text 변수에 저장
        text = response.get('message').get('text')
        chat_id = response.get('message').get('chat').get('id')

        # if 인사말이 오면, 나만의 인사해주기
        if '안녕' in text or 'hi' in text:
            text = '왔냐?'
        elif '로또' in text:
            text = sorted(random.sample(range(1, 46), 6))  

        # 마지막! url 만들어서 메시지 보내기
        api_url = f'{base_url}/sendmessage?chat_id={chat_id}&text={text}'
        requests.get(api_url)
    return 'OK', 200









if __name__ == '__main__':
    app.run(debug=True)