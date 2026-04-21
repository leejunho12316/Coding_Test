N = int(input())
meeting_list = []
for _ in range(N):
    m, n = map(int, input().split())
    meeting_list.append((m,n))

#1. 정렬
#끝나는 시간을 기준으로 오름차순 정렬해 최대한 많은 회의를 넣을 수 있도록 함.
#끝나는 시간이 같은 것들 중 시작 시간에 따라 오름차순으로 정리해 시작==끝인 회의도 넣을 수 있게 함.
meeting_list = sorted(meeting_list, key = lambda x : (x[1], x[0]), reverse=False)

cur_end = 0
count = 0
for meeting in meeting_list:

    #현재 meeting 시작 시간이 이전 meeting의 끝나는 시간 다음이라면
    if cur_end <= meeting[0]:
        cur_end = meeting[1]
        count += 1

print(count)
