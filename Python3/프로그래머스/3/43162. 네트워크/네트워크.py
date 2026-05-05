def solution(n, computers):
    answer = 0
    
    # 입력 받은 시작 index부터 DFS로 연결되어 있는 모든 노드 index를 반환하는 함수
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
    
    # 0부터 n-1까지 전체 index
    whole_idx = list(range(n))
    
    # 전체 index에서 하나라도 남아있다면
    while(whole_idx):
        # 전체 index 중 첫 번째 index부터 DFS 실행
        answer += 1
        visited_idx = dfs(whole_idx[0])
        # 입력한 원소와 연결되어있는 모든 노드 삭제
        whole_idx = [idx for idx in whole_idx if idx not in visited_idx]
    
    return answer