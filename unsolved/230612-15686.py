##################
## 15686번 
# 10:17~11:02 거의 손도 못댐
##################

from sys import stdin

N, M = map(int, stdin.readline().split())
city = list(list(map(int, stdin.readline().split())) for _ in range(N))
#print(city)

# 1에서 가까이에 있는 2들의 모든 정보를 다 담아야 할듯



##################
## 모범 코드
##################

## PJH 코드
from itertools import combinations
from sys import stdin

N, M = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for _ in range(N)]

houses = [[i, j] for i in range(N) for j in range(N) if city[i][j] == 1]
chickens = [[i, j] for i in range(N) for j in range(N) if city[i][j] == 2]

dists = [[abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]) for chicken in chickens] for house in houses]

total_dists = []
for selected in combinations(range(len(chickens)), M):
    total_dists.append(sum([min([dists[i][j] for j in selected]) for i in range(len(houses))]))

print(min(total_dists))


## KSI 코드
import itertools
n, m = map(int,input().split())
arr = [[] for i in range(n)]
house = []
chicken = []
for i in range(n):
    arr[i].extend(map(int,input().split()))
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])
ans = 1000000000
for c in itertools.combinations(chicken,m):
    distance_sum = 0
    for i in house:
        distance = 1000000000
        for j in c:
            distance = min(distance, abs(i[0] - j[0]) + abs(i[1] - j[1]))
        distance_sum += distance
    ans = min(ans, distance_sum)
print(ans)