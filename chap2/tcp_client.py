#!/usr/bin/python

import socket

# socket.AF_INETはIPv4を使う宣言のようなもの、socket.SOCK_STREAMはストリーム通信を使う宣言のようなもの
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 自分自身を指すIPアドレス(localhostで参照することもある)
ip = '127.0.0.1'
# ポート番号、49513~65535の間ならなんでも大丈夫なはず(プライベートポートと言い、自由に使えるポート番号)
port = 50000

server = (ip, port)
# serverで定めたipアドレスとport番号をもつサーバーと接続
sock.connect(server)

msg = ''
while msg != 'exit':
    # 標準入力からデータを取得、引数は標準入力を受け付ける時に表示されるだけで深い意味はない
    msg = input('->')

    # サーバにデータを送信
    # msgをencodeすることで、文字列型からバイト型に変換できる、文字列型とバイト型の違いは以下のリンク参照
    # https://qiita.com/hiroyuki_mrp/items/f0b497394f3a5d8a8395
    sock.send(msg.encode())

    # サーバからデータを受信
    data = sock.recv(1024)

    # バイト型から文字列型に変換するなら以下のコードがあったほうがいいと思う
    # data = data.decode()

    # サーバから受信したデータを出力
    print('Received from server: ' + str(data))

# 通信終了
sock.close()