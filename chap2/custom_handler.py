#!/usr/bin/python

from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # index.htmlファイルの読み込み
        html = open('index.html').read()
        # index.htmlファイルの中身をbytes型に変換
        html = bytes(html, encoding='utf-8')

        # クライアントに返送する応答を書き込む
        self.wfile.write(html)

ip = '127.0.0.1'
# 一般にwebサーバのport番号は80だが、他のwebサーバを起動していると使えないため、8000を指定したりすることが多い
port = 8000

handler = CustomHandler
server = HTTPServer((ip, port), handler)

server.serve_forever()