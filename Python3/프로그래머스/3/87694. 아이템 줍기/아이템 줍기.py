from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    #1.모든 좌표(사각형, 캐릭터, 아이템)에 2를 곱해서 확장한다.
    temp = []
    for rect in rectangle:
        rect = list(map(lambda x : x*2, rect))
        temp.append(rect)
    rectangle = temp
    
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    
    
    #2.board 배열(크기 약 100×100)을 만든다.
    board = [[-9] * 110 for _ in range(110)]
    
    #3.각 사각형을 순서대로 처리하면서:    
    # board[][] -> 왼쪽 위에서 시작하는 좌표
    # [[4, 4, 10, 10], [2, 6, 12, 8], [6, 2, 8, 12]] -> 왼쪽 밑에서 시작하는 좌표
    # 근데 길이만 같으면 되니까 상관없을듯
    for rect in rectangle:
        x1, y1, x2, y2 = rect[0], rect[1], rect[2], rect[3]
        
        #    3-1. 그 사각형의 내부(엄격한 부등호 조건)에 해당하는 점은 무조건 0
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0
        
        #    3-2. 그 사각형의 변에 해당하는 점은, 이미 0이 아닐 때만 1
        for x in range(x1, x2+1):
            if board[x][y1] != 0: board[x][y1] = 1
            if board[x][y2] != 0: board[x][y2] = 1
        for y in range(y1, y2+1):
            if board[x1][y] != 0: board[x1][y] = 1
            if board[x2][y] != 0: board[x2][y] = 1
        
    #4.캐릭터의 (2배) 좌표에서 시작해서, board값이 1인 점들만 상하좌우로 이동하는 BFS를 돌려 아이템의 (2배) 좌표까지의 최단 이동 횟수를 구한다.
    #queue에 넣는 순간에 visited. or queue에서 빼는 순간에 visited
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    character = (characterX, characterY, 0)
    queue = deque([character])
    visited = set()
    visited.add(character[:2])
    answer = 0
    
    while(queue):
        
        # queue pop하고 item 먹었으면 break
        cur_loc = queue.popleft()
        if (cur_loc[0], cur_loc[1]) == (itemX, itemY):
            answer = cur_loc[2]
            break
        
        # 네 방향 다 체크하고 1이면 queue에 넣으며 visitied 추가.
        for dir in directions:
            next_loc = (cur_loc[0] + dir[0], cur_loc[1] + dir[1], cur_loc[2] + 1)
            if next_loc[:2] not in visited and board[next_loc[0]][next_loc[1]] == 1:
                queue.append(next_loc)
                visited.add(next_loc[:2])
                

#### 총 이동 횟수 구하는데에서 끝남 (move)
        
    #5.구한 이동 횟수를 2로 나눠서 반환한다.
    
    return answer/2