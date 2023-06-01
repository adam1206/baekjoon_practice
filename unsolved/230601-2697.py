##################
## 2697번 
# 10:04~10:45 메모리 초과로 실패
# permutations를 사용하면 안되는 것 같음, 메모리 초과 발생
##################

import sys
from itertools import permutations # 기억 안나서 검색함

n = int(sys.stdin.readline())
for i in range(n):
    num = str(int(sys.stdin.readline()))
    num_list = list(permutations(num))
    
    sorted_list = sorted(list(map(''.join, num_list)))
    #print(''.join(num_list))
    
    for k in range(len(sorted_list)):
        if sorted_list[k] == num:
            if k == len(sorted_list)-1:
                print('BIGGEST')
                break
            else:
                print(sorted_list[k+1])
                break