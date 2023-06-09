##################
## 2565번 
# 10:02~10:45 해결법은 찾았으나 그걸 구현할 방법을 생각 못했음
##################
# 가장 긴 오름차순 찾는 방법 반드시 복습 후 맞춘 뒤 solved에도 기록하기

# 1 2 3 4 6 7 9 10
# 8 2 9 1 4 6 7 10 -> 가장 긴 오름차순 or 내림차순 찾기?
# a를 우선 오름차순으로 정렬하고
# 그거랑 매칭되는 b들 중 가장 긴 오름차순 or 내림차순을 찾아야 할 듯

n = int(input())
total_list = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    total_list.append(tmp)
    #print(total_list)
total_list.sort(key=lambda x: x[0])
#print(total_list)

up, down = 0, 0
for i in range(1, n):
    if total_list[i-1][1] < total_list[i][1]:
        up += 1
    elif total_list[i-1][1] > total_list[i][1]:
        down += 1
print(down + 1)