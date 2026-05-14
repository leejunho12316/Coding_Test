import heapq

def solution(N, road, K):
    answer = 0
    
    # 1. graph 생성
    graph = {n : {} for n in range(1,N+1)}
    for r in road:
        # 겹치면서 거리가 다른 경로가 있을 경우 최소값으로 저장.
        graph[r[0]][r[1]] = min(graph[r[0]].get(r[1], float('inf')), r[2])
        graph[r[1]][r[0]] = min(graph[r[1]].get(r[0], float('inf')), r[2])
        
        # graph[r[0]][r[1]] = r[2]
        # graph[r[1]][r[0]] = r[2]
        
    # 2. 최단 거리 저장 dict
    distances = {node: float('inf') for node in range(1, N+1)}
    distances[1] = 0
    
    # 3. heapq초기화 (현재 : 시작점 1)
    queue = []
    heapq.heappush(queue, [distances[1], 1])

    while queue:
        print(queue)
        
        cur_dist, cur_dest = heapq.heappop(queue)
        
        if distances[cur_dest] < cur_dist:
            continue
    
        for next_dest, weight in graph.get(cur_dest, {}).items():
            next_dist = cur_dist + weight
            
            if next_dist < distances[next_dest]:
                distances[next_dest] = next_dist
                heapq.heappush(queue, [next_dist, next_dest])
        
    
    print(f'graph : {graph}')
    print(f'distances : {distances}')
    
    answer = sum(1 for value in distances.values() if value <= K)
    
    return answer

