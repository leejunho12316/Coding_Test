from collections import deque

def solution(maps):

    n, m = len(maps), len(maps[0])
    
    #x 좌표, y좌표, 현재 count
    queue = deque([(0,0,1)])
    visited = set([])
    
    while(queue):
        
        row, col, count = queue.popleft()
        
        # 방문 체크 : visited check
        if (row, col) in visited:
            continue
        visited.add((row,col))
        
        # 상대 팀 진영 도달 체크 : x, y가 n-1, m-1이라면 return count
        if row==n-1 and col==m-1:
            return count
        
        
        # 동서남북 방향 전부 확인, tile 값이 1이면 queue에 그 좌표 append
        if row+1 < n and maps[row+1][col] == 1: # 남
            queue.append((row+1, col, count+1))
            
        if 0 <= row-1 and maps[row-1][col] == 1: # 북
            queue.append((row-1, col, count+1))
            
        if col+1 < m and maps[row][col+1] == 1: #동
            queue.append((row, col+1, count+1))
            
        if 0 <= col-1 and maps[row][col-1] == 1: #서
            queue.append((row, col-1, count+1))
    
    return -1
          
    
