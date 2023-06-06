##################
## 15663번 
# 10:05~10:55
# 틀렸지만 팀원들의 조언으로 고쳐서 맞음
# sorted는 str 타입과 int 타입에서 다르게 적용됨을 기억!!
##################
from itertools import permutations

n, m = input().split()
pool = list(map(int, input().split()))
answer_list = sorted(list(set(permutations(pool, int(m)))))
#print(answer_list)
for answer in answer_list:
    a = list(map(str, answer))
    print(' '.join(a))