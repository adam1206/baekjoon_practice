##################
## 1013번 
# 10:07~10:50 -> 패턴 파악하는데 시간 다 씀, 코드 제대로 짜보지도 못함
# 21:27~22:20 -> 정규표현식 구글링해서 재시도했지만 여전히 다 NO로 출력됨
##################

# 문자열의 최대 길이는 200
# 문자열의 어디서 잘라야 하며, 어떤 부분이 주어진 패턴안에 있는지 그걸 어떻게 알아내지...?
# ex1. 10010111 -> 1001 01 11(x)
# ex2. 011000100110001 -> 01 10001 0(x) 01 10001
# ex3. 0110001011001 -> 01 10001 01 1001

## 정규표현식 -> 구글링하여 방법 찾아봄
import sys
import re

n = int(sys.stdin.readline()) # stdin 사용법 또 잊어버려서 구글링 후 작성함
p = re.compile('(100+1+|01)+')

for i in range(n):
    pattern = str(sys.stdin.readline())
    m = p.match(pattern)
    #print(pattern, type(pattern))
    #print(m.group(), type(m.group())) # 인식된 패턴을 출력하려면 .group() 메소드를 사용하면 된다
    #print(str(pattern) == str(m.group()))
    if m.group() == pattern:
        print('YES')
    else:
        print('NO')
