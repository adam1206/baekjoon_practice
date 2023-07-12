##################
## 2296번
# 10:10 ~ 10:50 
##################
# x 좌표 기준으로 정렬한 다음에
# y값이 증가하는 경우랑 감소하는 경우로 dp 두개 사용해서 풀 수 있다고 함
# 가장 긴 증가하는 부분수열, 가장 긴 감소하는 부분수열
from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    x, y, c = map(int, stdin.readline().split())
    print(x, y, c)

