##################
## 1593번 
# 10:07~10:55 sort가 시간초과가 나서 딕셔너리나 다른 방법으로 재시도하기!
##################

# 문자열 S에서 길이 g 만큼씩을 봤을 때 그게 W를 이루고 있는 문자와 동일한지를 봐야함

# 예시)
# W: cAda / S: AbrAcadAbRa
# S의 Acad, cadA 부분이 W를 이루고 있는 문자와 동일하므로 답은 2
from sys import stdin

lenW, lenS = map(int, stdin.readline().split())
W = input()
S = input()
answer = 0

for i in range(lenS - lenW + 1):
    dict_W, dict_S = {}, {}
    for w in list(W):
        if w in dict_W:
            dict_W[w] += 1
        else:
            dict_W[w] = 1
    print(dict_W)
    for s in list(S[i:i+lenW]):
        if s in dict_S:
            dict_S[s] += 1
        else:
            dict_S[s] = 1
    print(dict_S)
    if dict_W == dict_S:
        print(dict_W, '=', dict_S)
        answer += 1
print(answer)
'''
# 이전에 시도했던 방법
for i in range(lenS - lenW + 1):
    #print(S[i:i+lenW])
    if set(S[i:i+lenW]) != set(W):
        print(set(S[i:i+lenW]), '!=', set(W))
        continue
    else:
        dict_W, dict_S = {}, {}
        for w in list(W):
            if w in dict_W:
                dict_W[w] += 1
            else:
                dict_W[w] = 1
        print(dict_W)
        for s in list(S[i:i+lenW]):
            if s in dict_S:
                dict_S[s] += 1
            else:
                dict_S[s] = 1
        print(dict_S)
        if dict_W == dict_S:
            print(dict_W, '=', dict_S)
            answer += 1
'''
