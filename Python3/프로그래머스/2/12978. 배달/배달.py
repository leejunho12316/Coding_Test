import heapq

#벨만-포드
def solution(N,road,K):
    answer = 0
    
    # 1. graph 생성
    graph = {n : {} for n in range(1,N+1)}
    for r in road:
        # 겹치면서 거리가 다른 경로가 있을 경우 최소값으로 저장.
        graph[r[0]][r[1]] = min(graph[r[0]].get(r[1], float('inf')), r[2])
        graph[r[1]][r[0]] = min(graph[r[1]].get(r[0], float('inf')), r[2])
    
    def bellman_ford(start_node):
        distances = {i : float('inf') for i in range(1, N+1)}
        distances[start_node] = 0
        has_cycle = False
        
        for _ in range(N-1):
            for start, ends in graph.items():
                for end, weight in ends.items():
                    if distances[start] != float('inf') and distances[start] + weight < distances[end]:
                        distances[end] = distances[start] + weight
        
        for _ in range(1):
            for start, ends in graph.items():
                for end, weight in ends.items():
                    if distances[start] != float('inf') and distances[start] + weight < distances[end]:
                        has_cycle = True
                        
        return distances, has_cycle
    
    d, has_cycle = bellman_ford(1)
    print(d, has_cycle)
    
    answer = sum(1 for value in d.values() if value <= K)

    return answer


# #다익스트라
# def solution(N, road, K):
#     answer = 0
    
#     # 1. graph 생성
#     graph = {n : {} for n in range(1,N+1)}
#     for r in road:
#         # 겹치면서 거리가 다른 경로가 있을 경우 최소값으로 저장.
#         graph[r[0]][r[1]] = min(graph[r[0]].get(r[1], float('inf')), r[2])
#         graph[r[1]][r[0]] = min(graph[r[1]].get(r[0], float('inf')), r[2])
        
#         # graph[r[0]][r[1]] = r[2]
#         # graph[r[1]][r[0]] = r[2]
        
#     # 2. 최단 거리 저장 dict
#     distances = {node: float('inf') for node in range(1, N+1)}
#     distances[1] = 0
    
#     # 3. heapq초기화 (현재 : 시작점 1)
#     queue = []
#     heapq.heappush(queue, [distances[1], 1])

#     while queue:
        
#         # 현재 위치
#         cur_dist, cur_dest = heapq.heappop(queue)
        
#         # 계산할 값어치가 있는지
#         if distances[cur_dest] < cur_dist:
#             continue
        
#         # 주변 노드 계산
#         for next_dest, weight in graph.get(cur_dest, {}).items():
#             next_dist = cur_dist + weight
            
#             if next_dist < distances[next_dest]:
#                 distances[next_dest] = next_dist
#                 heapq.heappush(queue, [next_dist, next_dest])
        
    
#     print(f'graph : {graph}')
#     print(f'distances : {distances}')
    
#     answer = sum(1 for value in distances.values() if value <= K)
    
#     return answer

