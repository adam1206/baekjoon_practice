##################
## 2668번 
# 10:03~10:50 못풀었음
##################

# 첫째줄 홀수 번째에는 홀수
# 둘째줄 짝수 번째에는 짝수
# 1 2 3 4 5 6 7 8 ... 98 99 100
# set() 사용해서 그냥 처음부터 쭉 탐색해야 할듯?
# 같은 위치에 같은 숫자부터 우선적으로 pick

from sys import stdin

N = int(stdin.readline())
first = [_ for _ in range(1, N+1)]
second, answer = [], []
for _ in range(N):
    second.append(int(stdin.readline()))
print(second)

for i, num in enumerate(second):
    if first[i] == num:
        answer.append(num)
print(answer)
