##################
## 18110번 
# 10:07~10:50, 11:36~11:54 어디에는 round 쓰고 어디에는 안쓰고 이러면서 헤메다가 결국 반올림 필요한 부분 직접 다 구현해서 맞춤!
##################

## 의견이 없으면 난이도는 0
## 30% 절사평균: 위에서 15%, 아래에서 15%를 제외하고 평균을 계산하는 방법
# 20명이 투표 -> 위에서 3명, 아래에서 3명의 의견은 제외하고 평균을 계산(반올림)

# 반올림이 round랑 뭐랑 다르게 작동했던 기억이 있는데... -> 맞음 이걸 반드시 기억하자!
from sys import stdin
from collections import deque

n = int(stdin.readline())
if n == 0:
    print(0)
else:
    # round 함수 작동 특이해서 직접 반올림 처리
    if (n * 0.15) - int(n * 0.15) >= 0.5:
        except_num = int(n * 0.15) + 1
    else:
        except_num = int(n * 0.15)
    level = deque([])
    for _ in range(n):
        level.append(int(stdin.readline()))
    #print(level)
    sorted_level = deque(sorted(level))
    #print(sorted_level, except_num)

    for _ in range(except_num):
        sorted_level.popleft()
        sorted_level.pop()
    #print(sorted_level)
    
    # round 함수 작동 특이해서 직접 반올림 처리
    full_num = sum(sorted_level)/len(sorted_level)
    int_num = sum(sorted_level)//len(sorted_level)
    #print(full_num, int_num)
    if full_num - int_num >= 0.5:
        print(int_num + 1)
    else:
        print(int_num)