def solution(tickets):
    
    tickets = sorted(tickets, reverse = False) # 정렬 : 알파벳순
    used = [False for _ in range(len(tickets))]
    answer = ["ICN"]
    
    
    def DFS(cur_ticket):
        #완료 조건 확인
        if len(answer) == len(tickets) + 1:
            #완료
            return True
        
        #동작
        for i, next_ticket in enumerate(tickets):
            if cur_ticket[1] == next_ticket[0] and not used[i]:
                used[i] = True
                answer.append(next_ticket[1])
                
                res = DFS(next_ticket)
                if res==True:
                    return True
                else:
                    used[i] = False
                    answer.pop(-1)
        
        #동작 실패
        return False
    
    DFS([None,"ICN"])
    
    return answer



