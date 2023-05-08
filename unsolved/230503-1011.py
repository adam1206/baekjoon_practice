##################
## 1011번 
# 주어진 예제는 맞췄으나 실제 정답은 아니었던 풀이
##################

# 규칙성 파악
# ex) 0 7 => 7-1=6, 6-1=5, 5-2=3, 3-3=0 // 7 = 1+2+2+1+1
# 1 -> 2 -> 3 -> 4 -> 남은 거리-1 -> 1
# 3-1 - 0 = 2  2-1=1 / 1-1=0
# 5-1 - 1 = 3  3-1=2 / 2-2=0
# 50-1 - 45 = 4  4-1=3 / 3-2=1 / 1-1=0

num_case = int(input())
for n in range(num_case):
    x, y = map(int, input().split()) # 이 부분 혼자 생각 못해냄!
    #print('x:', x, 'y:', y)
    d = y-x-1 # last 1 lightyear
    count = 1
    for i in range(y-x-1):
        if d - (i+1) >= 0:
            d -= (i+1)
            count += 1
            if d == 0:
                break
        else:
            count += 1
            break
    print(count)
