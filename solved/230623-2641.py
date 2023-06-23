#################
## 2641번
# 10:03~10:09, 10:17~10:49: 아슬아슬하게 맞춤!
#################

# 표본과 같은 지점에서부터 시작해서
# 패턴이 같으면 동일한 모양수열
# 파악해야 하는 모양수열들은 모두 길이 2배
# 표본과 순서가 정반대인 것도 만들었어야 함
length = int(input())
standard = list(map(int, input().split()))
reverse_standard = []
for s in standard:
    if s == 1 or s == 2:
        reverse_standard.append(s + 2)
    else:
        reverse_standard.append(s - 2)
# print(standard)
# print(reverse_standard)

test, answer = [], []
n = int(input())
for _ in range(n):
    tmp = list(map(int, input().split())) * 2
    test.append(tmp)

for t in test:
    for i in range(length):
        tmp2 = t[i : i + length]
        if tmp2 == standard or tmp2 == reverse_standard:
            answer.append(t[0:length])
        elif tmp2[::-1] == standard or tmp2[::-1] == reverse_standard:
            answer.append(t[0:length])
# print(answer)
print(len(answer))
for a in answer:
    tmp3 = ""
    for i in range(length):
        if i == length - 1:
            tmp3 += str(a[i])
        else:
            tmp3 += str(a[i]) + " "
    print(tmp3)
