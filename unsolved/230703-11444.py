#################
## 11444번
# 10:15~10:55 배열로는 절대로 못푸는 문제라고 함
# 나중에 참고할 사이트: https://cantcoding.tistory.com/28
#################

from collections import deque

n = int(input())
l = deque([0, 1])

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n - 1):
        tmp = l[-2] + l[-1]
        if tmp > 1000000007:
            tmp = tmp % 1000000007
        l.append(tmp)
        l.popleft()
        # print(l)
    print(l[-1] % 1000000007)
