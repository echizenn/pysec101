#!/usr/bin/python

import socket

# socket初期化(IPv4, ストリーム通信)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 50000

# ソケットにIPアドレスとポートを登録
sock.bind((host, port))
# 1クライアントからの接続要求を待ち受ける
sock.listen(1)

print('Waiting connection ...')

# コネクションとクライアントの情報が返ってくる
connection, addr = sock.accept()
print('Connection from: ' + str(addr))

while True:
    # クライアントからデータを送信、1024は一度に受信する最大サイズ
    data = connection.recv(1024)

    # クライアントからexitというデータが送られてきたら終了
    # b'exit'と'exit'の違いは、以下参照
    # https://qiita.com/hiroyuki_mrp/items/f0b497394f3a5d8a8395
    # 個人的には、dataをdecodeして比較した方がわかりやすい気がします、そうすればそのあとのprint文でb'~'ではなく、通常の文字列で表示されます
    # data = data.decode()
    # if data == 'exit':
    if data == b'exit':
        break

    print('Received a message: ' + str(data))

    # クライアントにデータを送信
    # data = data.encode()
    connection.send(data)
    print('Sent a message: ' + str(data))

# connectionとsocketをクローズ
connection.close()
sock.close()