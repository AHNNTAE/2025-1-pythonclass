# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가?
# 규칙: n이 짝수 -> n/2
#     n이 홀수 -> 3  * n + 1
# 예: 5-> 16 -> 8 -> 4 -> 2 ->1 (5단계)






# if n % 2 == 1:
#      print('n은 홀수')
# else:
#     print('n은 짝수')


# def collatz_steps(n):
#     """주어진 n이 1이 될 때까지의 콜라츠 단계 수 계산"""
#     steps = 0
#     while n != 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3 * n + 1
#         steps += 1
#     return steps
#
#
# # 1부터 1000까지 가장 긴 단계를 거치는 수 찾기
# max_steps = 0
# number_with_max_steps = 0
#
# for num in range(1, 1001):
#     steps = collatz_steps(num)
#     if steps > max_steps:
#         max_steps = steps
#         number_with_max_steps = num
#
# print(f"가장 긴 단계를 거치는 수: {number_with_max_steps}, 단계 수: {max_steps}")


n = 9

#단계의 갯수를 셀것
#n을 1부터 99까지 변화하면서, 각각의 단계수를 출력할 것
#그중 가장 큰 수를 찾을 것
while n != 1:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n / 2
    print(n)




