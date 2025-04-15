def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# 1부터 100까지의 숫자와 해당 단계 수를 튜플로 저장
results = [(n, collatz_steps(n)) for n in range(1, 101)]

# 단계 수 기준으로 내림차순 정렬
results.sort(key=lambda x: x[1], reverse=True)

# 상위 3개 출력
print("단계 수가 가장 큰 상위 3개 숫자:")
for i in range(3):
    print(f"{i+1}번째: 숫자 = {results[i][0]}, 단계 수 = {results[i][1]}")
