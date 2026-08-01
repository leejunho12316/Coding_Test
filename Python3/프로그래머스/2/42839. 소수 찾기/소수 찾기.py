from itertools import permutations

def is_sosu(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,x):
        if x%i==0:
            return False
    
    return True

def solution(numbers):
    
    whole_list = []
    for i in range(1, len(numbers)+1):
        
        for j in [int(''.join(temp)) for temp in list(permutations(numbers, i))]:
            whole_list.append(j)
        
    
    print(whole_list)
    whole_list = list(set(whole_list))
    
    answer = 0
    for number in whole_list:
        if is_sosu(number):
            answer+=1
            
    return answer
    