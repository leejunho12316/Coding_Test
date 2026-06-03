import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(scoville[0] < K):            #스코빌 지수가 다 K 이상인지 확인
        if len(scoville) <= 1:          #섞을 수 있는지 확인. 없으면 -1
            return -1
        
        item1 = heapq.heappop(scoville) #섞어섞어
        item2 = heapq.heappop(scoville)
        item3 = item1 + item2*2
        heapq.heappush(scoville, item3)
        answer += 1    

    return answer

# min(heapqueue)와 heapqueue[0]로 최솟값 접근할 때 시간 차이가 크다