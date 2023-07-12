#################
## 1897번
# 11:10~11:50 제대로 파악 못함
#################
from sys import stdin

d, word = input().split()
# print(d, word, type(d), type(word))

word_list = []
for _ in range(int(d)):
    tmp = stdin.readline().strip()
    word_list.append(tmp)
    print(word_list)

## 너비 탐색? 으로 접근해야 하는듯
