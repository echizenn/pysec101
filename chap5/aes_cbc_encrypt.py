#!/usr/bin/python

from aes_functions import key_schedule, AddRoundKey, SubBytes, ShiftRows, MixColumns
import numpy as np
import sys
import hashlib

def encrypt_1block(key, text):
    roundkeys = key_schedule(key)
    roundkeys = np.array([rk.reshape(4, 4).T for rk in roundkeys])
    text = text.reshape(4, 4).T

    out = AddRoundKey(text, roundkeys[0])
    for i in range(1, 10):   # ラウンド2~10
        out = SubBytes(out)
        out = ShiftRows(out)
        out = MixColumns(out)
        out = AddRoundKey(out, roundkeys[i])
    out = SubBytes(out)
    out = ShiftRows(out)
    out = AddRoundKey(out, roundkeys[-1])
    return list(out.T.reshape(16,))

def encrypt(key, text):
    iv = hashlib.md5(key+b'key').digest()  # 初期化ベクトルの作成
    iv = list(iv)

    key = np.array(list(key))
    text = [text[i:i+16] for i in range(0, len(text), 16)]   # 16バイトで区切る
    cipher = iv                 # 初期化ベクトルを暗号文に含める

    last_result = np.array(iv)  # 最初のブロックではivを前回の結果として使う
    for t in text:
        t = np.array(list(t))
        last_result = encrypt_1block(key, last_result^t)  # 前回の結果とのXORが引数になる
        cipher += last_result
    return cipher


if __name__=='__main__':
    f_key = open(sys.argv[1], 'rb')
    f_txt = open(sys.argv[2], 'rb')
    key = f_key.read()
    text = f_txt.read()

    output = encrypt(key, text)
    f_out = open('output.dat', 'wb')
    f_out.write(bytearray(output))

    f_key.close()
    f_txt.close()
    f_out.close()