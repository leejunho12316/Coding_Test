from collections import deque

# 단어끼리 알파벳 하나만 다른지 확인하는 함수
def _is_only_one_diff(str1, str2):
    res = sum([1 for a, b in zip(str1, str2) if a!=b])
    
    if res==1:
        return True
    return False

def solution(begin, target, words):
    
    begin = (begin, 0)
    
    visited = set()
    visited.add(begin[0])
    queue = deque([begin])
        
    while(queue):
        
        cur = queue.popleft()
        if cur[0] == target:
            return cur[1]
        
        for word in words:
            if word not in visited and _is_only_one_diff(word, cur[0]):
                queue.append((word, cur[1] + 1))
                visited.add(word)
        
    return 0