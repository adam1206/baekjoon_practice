#################
## 20159번
# 10:24~11:09 밑장 빼기를 잘못 이해함
# 밑장은 무조건 맨 아래 숫자! 밑장을 빼는 순간 순서가 뒤바뀜

#################
# 리스트 X를 짝수번째를 기준으로 나눈 뒤
# 기본적으로 홀수번째 수들을 더한 값들을 가져가야 하지만
# 딱 1번 짝수번째 수를 더할 수 있는 기회가 있어야 함

N = int(input())
X = list(map(int, input().split()))

# 일단 정훈이가 가져가는 카드(홀수번째)보다 상대가 가져가는 카드의 수가
# 더 큰 경우들만 전부 파악하여 check에 저장
check = []
for i, v in enumerate(X):
    if i % 2 == 0:
        if X[i] < X[i + 1]:
            check.append([i, X[i + 1]])
# print(check)

if len(check) == 0:
    answer = 0
    for i, v in enumerate(X):
        if i % 2 == 0:
            answer += v
    print(answer)
else:
    total = [0] * (N // 2)
    # print(total)
    index = 0
    for n in range(len(check)):
        for i, v in enumerate(X):
            if i % 2 == 0:
                if i == check[index][0]:
                    # print("i:", i, "check:", check[index][0])
                    total[n] += X[i + 1]
                else:
                    total[n] += X[i]
        index += 1
    # print(total)
    print(max(total))
