##################
## 3216번 
# 10:02~10:45
# input: 노래 길이, 다운로드 걸리는 시간
# 2 1 3 2 : 노래 길이의 앞부분 누적 합
# 1 5 3(1/2) 4 : 남은 다운로드 뒷부분 누적 합
# 마지막 곡 다운이 끝날 때 시간 = 마지막 곡 이전까지의 노래 재생 시간
# music = [2, 3, 6, 8]
# download = [1, 5, 3, 4]
##################

import sys

n = int(sys.stdin.readline())
music, download = [], []
for _ in range(n):
    m, d = map(int, sys.stdin.readline().split())
    if len(music) == 0:
        music.append(m); download.append(d)
    else:
        m_sum = music[-1]
        music.append(m); download.append(d)
        music[-1] += m_sum
    #print(music, download)

# music[-2]와 download의 뒤에서부터 합을 비교
download_r = download[::-1]
sum_r, count, answer = 0, 0, 0
for r in download_r:
    if count == 1:
        answer += r
        continue
    sum_r += r
    #print('작동', sum_r)
    if sum_r >= music[-2]:
        count += 1
        answer += (sum_r - music[-2])

print(answer)