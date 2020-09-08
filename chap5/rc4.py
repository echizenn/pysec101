#!/usr/bin/python

import sys

def KSA(K):
    S = list(range(256))   # listじゃないとi番目とかできないような
    j = 0
    for i in range(256):
        j += S[i] + K[i % len(K)]    # Kを0~len(K)で循環させる
        j %= 256
        S[i], S[j] = S[j], S[i]      # swap
    return S

def PRGA(S, plain):
    j = 0
    Z = []     # 文字列にappend使えない
    for i in range(1, len(plain)+1):
        i %= 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]         # swap
        Z.append(str(S[(S[i]+S[j]) % 256]))  # 擬似乱数の生成、str型に変換する
    return ''.join(Z)   # 文字列にして返す

def RC4(key, text):
    key = list(key)
    text = list(text)
    S = KSA(key)
    Z = PRGA(S, text)
    out = [text[i] ^ int(Z[i]) for i in range(len(text))]  # 結果もint型のリストにする
    return out

if __name__=='__main__':
    f_key = open(sys.argv[1], 'rb')
    f_txt = open(sys.argv[2], 'rb')
    key = f_key.read()
    text = f_txt.read()

    output = RC4(key, text)
    f_out = open('output.dat', 'wb')
    f_out.write(bytearray(output))

    f_key.close()
    f_txt.close()
    f_out.close()