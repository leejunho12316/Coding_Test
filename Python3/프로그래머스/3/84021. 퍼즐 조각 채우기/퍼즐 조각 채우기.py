from collections import deque

def 덩어리(table, target):
    
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    result_lst = []
    
    width = len(table)
    for i in range(width):
        for j in range(width):
            visited = set()
            if table[i][j] == target:

                cur_node = (i,j)

                queue = deque([cur_node])
                visited.add(cur_node)

                while(queue):
                    cur_node = queue.popleft()

                    for dir in directions:
                        next_node = (cur_node[0] + dir[0], cur_node[1] + dir[1])
                        #next_node 범위 확인
                        if 0 <= next_node[0] and next_node[0] < width and 0<=next_node[1] and next_node[1] < width:
                            # 조건 확인
                            if table[next_node[0]][next_node[1]] == target and next_node not in visited:
                                # 다음 방문할 노드에 추가
                                queue.append(next_node)
                                visited.add(next_node)
                
                #방문한 것 1로 처리하고 결과에 저장
                for v in visited:
                    table[v[0]][v[1]] = (target + 1)%2 #-> 와 지렸다
                result_lst.append(sorted(list(visited)))
                            
    return result_lst

def normalize(puzzles):
    
    new_puzzles = []
    
    for puzzle in puzzles:
        row_min = min([p[0] for p in puzzle])
        col_min = min([p[1] for p in puzzle])
        
        result = []
        for p in puzzle:
            result.append((p[0]-row_min, p[1]-col_min))
        
        new_puzzles.append(result)
        
    return new_puzzles

def rotate(puzzle):
    new_puzzle = []
    
    for p in puzzle:
        R = max([p[0] for p in puzzle]) + 1
        new_puzzle.append((p[1], R-1-p[0]))

    return sorted(new_puzzle)

def solution(game_board, table):
    
    #1. 덩어리 뽑기 : 보드와 table에서 BFS로 각각 퍼즐 조각 뽑기
    game_board_puzzles = 덩어리(game_board, 0)
    table_puzzles = 덩어리(table, 1)
    
    #2. 정규화 & 정렬 : 좌표값 정규화 & 정렬
    game_board_puzzles = normalize(game_board_puzzles)
    table_puzzles = normalize(table_puzzles)
    
    #3. 회전하며 매칭 확인
    # 원래 행 + 회전후 열 = R-1
    # 원래 열 = 회전후 행
    answer = 0
    t_used = [False for _ in range(len(table_puzzles))]
    g_used = [False for _ in range(len(game_board_puzzles))]
    
    for ti, tp in enumerate(table_puzzles):
        for gi, gp in enumerate(game_board_puzzles):
                        
            if not t_used[ti] and not g_used[gi]:
                for _ in range(4):
                    tp = rotate(tp)
                    if tp == gp:
                        answer += len(tp)
                        t_used[ti] = True
                        g_used[gi] = True
                        break

    return answer