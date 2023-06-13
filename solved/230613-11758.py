##################
## 15686번 
# 10:05 ~ 10:50 마지막에 힌트 받아서 맞은 문제
# 기억! 나누기 연산은 지양하자!!
##################

## 처음 두 점 P1, P2를 이은 직선을 기준으로
# 직선보다 위에 있으면 반시계
# 직선보다 아래에 있으면 시계
# 직선상에 있으면 일직선
# 직선의 식을 만들어야 겠다

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if (y3 - y1)*(x2 - x1) > (y2-y1) * (x3 - x1):
    print(1)
elif (y3 - y1)*(x2 - x1) < (y2-y1) * (x3 - x1):
    print(-1)
else:
    print(0)

# 직선의 방정식 세울 때 나누기를 하면 뭔가 문제가 생기는듯
# 아래처럼 풀었을 때는 채점 되다가 틀렸음
'''
if x1 == x2:
    if x3 > x1:
        print(1)
    elif x3 < x1:
        print(-1)
    else:
        print(0)
elif y1 == y2:
    if y3 > y1:
        print(1)
    elif y3 < y1:
        print(-1)
    else:
        print(0)
else:
    if (y3 - y1)*(x2 - x1) > (y2-y1) * (x3 - x1):
        print(1)
    elif (y3 - y1)*(x2 - x1) < (y2-y1) * (x3 - x1):
        print(-1)
    else:
        print(0)
'''