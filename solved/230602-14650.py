##################
## 14650번 
# 10:04~10:45
# 중복순열 product를 썼는데 시간초과는 아니고 그냥 틀림
# 틀린 이유가 print가 아닌 return으로 제출해서였음
##################

# 3의 배수의 특징: 각자리 숫자의 합이 3의 배수
from itertools import product

key = ['0', '1', '2']

def solution():
    answer = 0
    n = int(input())
    if n == 1:
        print(0)
    else:
        tmp = list(product(key, repeat=n))
        fin = list(map(int, map(''.join, tmp)))
        for f in fin:
            if len(str(f)) != n:
                continue
            if f % 3 == 0:
                answer += 1
        print(answer)

solution()

# 하지만 내 풀이는 n이 큰 경우에는 쓸 수 없는 풀이
# n이 큰 경우에는 다음과 같이 3의 배수의 특징을 잡는 식으로 코드를 짜야 함
'''
print(2 * int(3 ** (int(input()) - 2)))
'''