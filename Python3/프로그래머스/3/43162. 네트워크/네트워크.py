def solution(n, computers):
    answer = 0
    
    # 입력 받은 index로부터 연결되어 있는 모든 노드들의 index를 DFS로 반환하는 함수
    def dfs(start_idx):
        
        stack = [start_idx]
        visited = set([])
        
        while stack:
            #현재 노드
            cur_idx = stack.pop()
            cur_list = computers[cur_idx]

            #방문 노드 확인
            if cur_idx in visited:
                continue

            visited.add(cur_idx)

            #stack에 다음 방문할 노드 추가
            ones = [i for i, v in enumerate(cur_list) if v == 1]

            for i in ones:
                stack.append(i)
        
        return list(visited)
    
    # 0부터 n-1까지 전체 node
    whole_idx = list(range(n))
    
    # 전체 node 순회
    while(whole_idx):
        # 남아있는 node 중 첫 번째 DFS 실행
        visited_idx = dfs(whole_idx[0])
        # 현재 node 연결되어있는 모든 노드 삭제
        whole_idx = [idx for idx in whole_idx if idx not in visited_idx]
        
        # 네트워크 개수 +1
        answer += 1
    
    return answer