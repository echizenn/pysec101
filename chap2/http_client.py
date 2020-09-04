#!/usr/bin/python

import requests

url = 'http://localhost:8000'
# HTTPリクエストを送信して、レスポンスをresponseに代入
response = requests.get(url)
print(response.text)