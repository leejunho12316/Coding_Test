def solution(citations):
    
    answers = []
    for h in range(0, len(citations) + 1):
        h_more = len([i for i in citations if h<=i])
        h_less = len([i for i in citations if h>i])
        
        if h_more >= h and h_less <= h:
            answers.append(h)
    
    return max(answers)