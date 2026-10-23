import time
import random

sm = list(m)
random.shuffle(sm)
sm = ''.join(sm)

em = m

while 1:
    for i in range(1000):
        st = time.time()
        ida_star('123456000')
        et = time.time()
        res = et - st
        print("실행 시간: {:.5f}초".format(res))
