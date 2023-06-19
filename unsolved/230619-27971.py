#################
## 27971번
# 10:06~10:51 어려워서 거의 손도 못댐...
#################

""" 버려진 코드
# 한 구간이 다른 구간과 겹치면 합침
# 겹치지 않으면 새로운 구간으로 append
zone = []
for _ in range(M):
    left, right = map(int, stdin.readline().split())
    if len(zone) == 0:
        zone.append([left, right])
    else:
        for i, z in enumerate(zone):
            print(z[0], z[1])
            if z[0] > right:
                zone.append([left, right])
            elif z[1] < left:
                zone.append([left, right])
            else:
                zone[i] = [min(z[0], left), max(z[1], right)]
"""

from sys import stdin

N, M, A, B = map(int, stdin.readline().split())

# 그냥 일단 다 zone에 append
zone = []
for _ in range(M):
    left, right = map(int, stdin.readline().split())
    zone.append([left, right])
print(zone)
