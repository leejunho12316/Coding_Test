def solution(answers):
    
    type1, type2, type3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0]
    
    for i, v in enumerate(answers):
        if answers[i] == type1[i % len(type1)]: correct[0] += 1
        if answers[i] == type2[i % len(type2)]: correct[1] += 1
        if answers[i] == type3[i % len(type3)]: correct[2] += 1
    
    m = max(correct)
    mask = [True if c == m else False for c in correct]
    
    result = []
    for i, v in enumerate(correct):
        if mask[i]:
            result.append(i+1)
            
    return result
    
    