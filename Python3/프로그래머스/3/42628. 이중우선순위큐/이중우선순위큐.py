import heapq

#일반 heapq는 최솟값이 root에 있다는 것만 보장하고 나머지 전체는 신경 안씀.
# 부호반전을 통해 최대/최소값이 root에 계속 바뀌어 오도록 하면 될듯.
# is_reversed가 False 일때는 최소값이 맨 위, True 일때는 최대값이 맨 위.
def heapq_reverse(queue):
    queue = [-q for q in queue]
    heapq.heapify(queue)
    
    return queue

def solution(operations):
    answer = 0
    is_reversed = False
    
    queue = []
    heapq.heapify(queue)
       
    for oper in operations:
        if "I" in oper:
            number = int(oper.split(' ')[1])
            
            #뒤집힘 여부에 따라 부호 변경. heapq를 뒤집히지 않은 상태로 유지하는것보다 효율적.
            if is_reversed :
                number = -number
            
            heapq.heappush(queue, int(number))

        #reversed되어 있지 않다면 해서 최댓값 pop
        elif queue and oper == "D 1":
            if not is_reversed:
                queue = heapq_reverse(queue)
                is_reversed = True
            heapq.heappop(queue)
            
        #reversed되어 있다면 해서 최소값 pop
        elif queue and oper == "D -1":
            if is_reversed:
                queue = heapq_reverse(queue)
                is_reversed = False
            heapq.heappop(queue)
        
    if is_reversed:queue = heapq_reverse(queue)
        
    if queue:
        return [max(queue), min(queue)]
    return [0,0] 
