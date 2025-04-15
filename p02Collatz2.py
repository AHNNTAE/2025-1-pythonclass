import statistics
from turtledemo.penrose import start

#2025409 우박수프로젝트 두번째 : 기본 통계량 구하기
#넘파이 배열, 리스트 두가지 방식으로 시험
#구하는 통계량: 평균, 중앙값, 표준편자,최빈값

import numpy as np
from numpy.ma.core import append

from p02Collatz import ncount

ncounta = np.zeros(100)
ncountl = []

for n in range(1, 100):
    ncount = 0
    i = n

    while i != 1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i // 2
        ncount = ncount + 1

    ncountl.append(ncount)

import  statistics
print(ncountl)
print(sum(ncountl) / len(ncountl))


import time
import statistics
import numpy as np

MAXNUM = 1000

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    return count

ncountL = []

start = time.time()
for n in range(1, MAXNUM):
    ncount = collatz(n)
    ncountL.append(ncount)

print(f'최대값     = {max(ncountL)}')
print(f'평균       = {statistics.mean(ncountL):.2f}')
print(f'중앙값     = {statistics.median(ncountL)}')
print(f'최빈값     = {statistics.mode(ncountL)}')
print(f'표준편차   = {statistics.stdev(ncountL):.2f}')
end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다!')

# NumPy 배열 사용 버전
start = time.time()
ncounta = np.zeros(MAXNUM - 1)
for n in range(1, MAXNUM):
    ncount = collatz(n)
    ncounta[n - 1] = ncount
end = time.time()
print(f'(NumPy 버전) {end - start:.5f} 초가 걸렸습니다!')



