##################
## 2872번 
# 10:25~10:55 시간초과 뜸
##################
# 알파벳순 정렬: 가장 앞서는 책을 맨 위, 가장 뒤 책을 맨 아래
# 책 하나를 뺀 다음 가장 위에 추가(appendleft)

import sys
from collections import deque

n = int(sys.stdin.readline())
books = deque([])
for i in range(n):
    tmp = int(sys.stdin.readline())
    books.append(tmp)

answer = deque(sorted(books))
count = 0
while books != answer:
    print(books, answer)
    for j in range(n-1):
        if books[j] > books[j+1]:
            tmp2 = books[j+1]
            del books[j+1]
            books.appendleft(tmp2)
            count += 1
            break
print(count)
