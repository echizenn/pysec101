#!/usr/bin/python

import sys
import string
import random
from subprocess import PIPE
import subprocess

class Fuzzer(object):
    def __init__(self, target):
        self.target = target
        self.alnum = string.digits + string.ascii_letters
        self.rand = random.SystemRandom()

    def gen_fuzz(self):
        rand_int = self.rand.randint(1, 64)   # ファズの文字数
        fuzz = random.choices(self.alnum, k=rand_int)
        fuzz = ''.join(fuzz)
        return fuzz

    def do_fuzz(self, fuzz):
        cmd = ' '.join([self.target, fuzz])
        ret = subprocess.run(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        ret_code = ret.returncode
        return ret_code

    def dump(self, fuzz, ret_code):
        data = str(ret_code) + ',' + fuzz + '\n'
        f = open('dump.csv', 'a')
        f.write(data)
        f.close()


def main():
    target = sys.argv[1]
    fuzzer = Fuzzer(target)

    fuzz_cnt = 0
    crash = 0
    while True:     # 個人的に1よりTrueの方がわかりやすいと思うので変えました
        fuzz = fuzzer.gen_fuzz()
        fuzz_cnt += 1
        ret_code = fuzzer.do_fuzz(fuzz)
        if ret_code > 0:
            crash += 1
            fuzzer.dump(fuzz, ret_code)
        sys.stdout.write('\rfuzz: %d, crashes: %d' % (fuzz_cnt, crash))
        sys.stdout.flush()


if __name__=='__main__':
    main()