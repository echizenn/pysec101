#!/usr/bin/python

from http.server import HTTPServer, SimpleHTTPRequestHandler

ip = '127.0.0.1'
# 一般にwebサーバのport番号は80だが、他のwebサーバを起動していると使えないため、8000を指定したりすることが多い
port = 8000

# SimpleHTTPRequestHandlerでは、現在のディレクトリ以下にあるファイルを、HTTP リクエストにおけるディレクトリ構造に直接対応付けて提供する。
handler = SimpleHTTPRequestHandler
server = HTTPServer((ip, port), handler)

# クライアントとの接続を待つ
server.serve_forever()