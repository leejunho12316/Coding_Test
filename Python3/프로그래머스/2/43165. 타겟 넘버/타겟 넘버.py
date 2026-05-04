def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(i, sum):
        global answer

        if i == len(numbers): #최대 횟수 끝났으면
            if sum == target:
                answer += 1
            return
                
        dfs(i + 1, sum + numbers[i])
        dfs(i + 1, sum - numbers[i])
    
    dfs(0, 0)
    
    return answer