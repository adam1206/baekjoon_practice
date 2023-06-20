#################
## 1780번
# 10:07~10:52 뭔가 방법은 알겠는데 못풀었음
## 분할 정복-재귀를 공부하고 재도전!
#################

# 이렇게 행렬 형태를 줄로 입력받아서 푸는 문제
# 항상 어려워했고, 지금도 잘 모르겠음
# 그래도 일단 같은 숫자로만 채워진 경우를 판단하는 것은
# set()을 사용해서 1종류만 나오면 세는 방식으로 하면 될듯

"""
[[0, 0, 0, 1, 1, 1, -1, -1, -1], 
 [0, 0, 0, 1, 1, 1, -1, -1, -1], 
 [0, 0, 0, 1, 1, 1, -1, -1, -1],
 [1, 1, 1, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 1, -1, 0, 1, -1, 0, 1, -1],
 [0, -1, 1, 0, 1, -1, 0, 1, -1],
 [0, 1, -1, 1, 0, -1, 0, 1, -1]]
"""
from sys import stdin

N = int(stdin.readline())
# N: 1, 3, 9, 27, 81, 243, 729, 2187

paper, answer = [], []
for _ in range(N):
    tmp = list(map(int, stdin.readline().split()))
    paper.append(tmp)
print(paper)

# N을 3으로 나누어 반복 탐색하고 이 값이 1이 되는 순간이 마지막임
# append 말고 리스트 합치는게 뭐였지
# extend 였던 것 같은데
while N > 1:
    for i in range(0, N, N // 3):  # i = 0, 1/3N, 1/2N
        first, second, third = [], [], []
        for j in range(N // 3):
            first.extend(paper[i + j][0 : N // 3])
            second.extend(paper[i + j][N // 3 : N // 3 * 2])
            third.extend(paper[i + j][N // 3 * 2 : N])
        print(first, second, third)
    N = N // 3
