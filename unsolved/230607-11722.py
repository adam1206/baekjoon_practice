#################
## 11722번
# 10:28~10:58
#################

# 10 60 40 50 20 30 70 60 50 40 30 20
# 모든 가능한 감소하는 부분 수열의 길이를 전부 기록해서
# 리스트에 담은 다음 그 중 max를 출력?
# 알고리즘: DP
length = int(input())
a = list(map(int, input().split()))
print(a)
num_list, prev_num = [], 0
for num in a:
    if num > max_num:
        max_num = num
        num_list.append(1)
