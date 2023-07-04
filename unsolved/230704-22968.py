##################
## 22968번
# 10:07~ 10:50 : DP(동적 프로그래밍)로 풀어야 하는 문제라고 함
# 참고 사이트: https://softyong.tistory.com/7
##################

from sys import stdin

n = int(stdin.readline())
answer = []
# 1 / 2,3 / 4~7 / 8~15 / 16~31 / 32~63 ...
# 트리 문제를 가장한 2의 거듭제곱 문제라고 생각하여 코드를 작성하였음
for _ in range(n):
    v = int(stdin.readline())
    for i in range(43):
        if v >= 2**i and v < 2**(i+1):
            answer.append(i+1)
            break

for j in range(len(answer)):
    print(answer[j])