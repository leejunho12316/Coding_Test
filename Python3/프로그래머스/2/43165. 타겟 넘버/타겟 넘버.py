# stack dfs
def solution(numbers, target):
    
    answer = 0
    stack = [(0,0)]
    
    while stack:
        # stack으로부터 하나 꺼내기
        ind, sum = stack.pop()
        
        # 조건 확인
        if ind == len(numbers):
            if sum == target:
                answer += 1
            continue
            
        # 분기 2개 stack에 저장
        stack.append((ind + 1, sum + numbers[ind]))
        stack.append((ind + 1, sum - numbers[ind]))
        
    return answer


# 재귀 dfs
# def solution(numbers, target):
#     global answer
#     answer = 0
    
#     def dfs(i, sum):
#         global answer

#         if i == len(numbers): #최대 횟수 끝났으면
#             if sum == target:
#                 answer += 1
#             return
                
#         dfs(i + 1, sum + numbers[i])
#         dfs(i + 1, sum - numbers[i])
    
#     dfs(0, 0)
    
#     return answer