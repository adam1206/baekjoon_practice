##################
## 1012번 
# 10:06~10:10:45
# 서로 붙어있는 1의 개수를 알면 되는구나
# 담는 그릇을 이중 리스트로 생각해서 인접한 좌표는
# 같은 리스트에, 인접하지 않은 좌표는 다른 리스트에
# 넣는 식으로 짜면 될 것 같음
##################

import sys

n = int(sys.stdin.readline())
for i in range(n):
    garo, sero, total = map(int, sys.stdin.readline().split())
    #print(garo, sero, total)
    answer = []
    for t in range(total):
        x, y = map(int, sys.stdin.readline().split())
        if len(answer) == 0:
            answer.append([(x, y)])
            print(answer)
        else:
            for a in answer:
                if (x-1, y) or (x+1, y) or (x, y-1) or (x, y+1) in a:
                    a.append((x, y))
                    print(answer)
                else:
                    answer.append([(x, y)])
                    print(answer)
    print(len(answer))