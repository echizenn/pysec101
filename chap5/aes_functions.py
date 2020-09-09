#!/usr/bin/python

import numpy as np

Rcon = np.array([
    [0x01, 0x00,  0x00,  0x00],
    [0x02, 0x00,  0x00,  0x00],
    [0x04, 0x00,  0x00,  0x00],
    [0x08, 0x00,  0x00,  0x00],
    [0x10, 0x00,  0x00,  0x00],
    [0x20, 0x00,  0x00,  0x00],
    [0x40, 0x00,  0x00,  0x00],
    [0x80, 0x00,  0x00,  0x00],
    [0x1b, 0x00,  0x00,  0x00],
    [0x36, 0x00,  0x00,  0x00],
])

def key_schedule(key):
    W = key.reshape(4, 4)         # 4*4の行列形式に変換
    for i in range(4, 44):
        W_i = None
        if i%4 == 0:
            tmp = np.roll(W[i-1], -1, axis=0)       # RotWord
            tmp = np.array([S_box[t] for t in tmp]) # SubWord
            tmp ^= Rcon[i/4-1]
            W_i = W[i-4] ^ tmp
        else:
            W_i = W[i-4] ^ W[i-1]
        W = np.vstack([W, W_i])
    return W.reshape(11, 16)