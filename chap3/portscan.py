#!/usr/bin/python

import socket, sys

# コマンドライン引数を取得(python portscan.py aとして実行するときはaがipに代入される)
ip = sys.argv[1]

ports = range(1, 10000)  # 1~10000のポートを確認する

for port in ports:
    sock = socket.socket()
    ret = sock.connect_ex((ip, port))

    if ret == 0:
        print(str(port) + " open")