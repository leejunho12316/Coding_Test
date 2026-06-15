import heapq

def solution(jobs):
    
    jobs = sorted(enumerate(jobs), key = lambda x : x[1][0] )
    
    answer = 0
    completed, n = 0, len(jobs)
    job_idx = 0
    cur_time = 0
    queue = [] #작업 시간, 요청 시간, 아이디
    
    while completed < n:
        
        #현재 시각까지 요청해야하는 작업 전부 queue에 추가
        while job_idx < n and jobs[job_idx][1][0] <= cur_time:
            id, (req_time, working_time) = jobs[job_idx]
            heapq.heappush(queue, (working_time, req_time, id))
            job_idx += 1
        
        #대기열에서 하나 실행.
        if queue:
            working_time, req_time, id = heapq.heappop(queue)
            cur_time += working_time
            answer += (cur_time - req_time)
            completed += 1
        else:
            cur_time = jobs[job_idx][1][0]
            
    return answer // n
        
        