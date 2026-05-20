import heapq

# 벨만-포드
def solution(n, s, a, b, fares):
    edges = []
    for c, d, f in fares:
        edges.append((c,d,f))
        edges.append((d,c,f))
    
    def bellman_ford(start_node):
        distances = {i:float('inf') for i in range(1, n+1)}
        distances[start_node] = 0
        has_cycle = False
        
        for _ in range(n-1):
            for start, end, weight in edges:
                if distances[start] != float('inf') and distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight
        
        for _ in range(1):
            for start, end, weight in edges:
                    if distances[start] != float('inf') and distances[start] + weight < distances[end]:
                        has_cycle = True
                        
        return distances, has_cycle
    
    distances_s, s_has_cycle = bellman_ford(s)
    distances_a, a_has_cycle = bellman_ford(a)
    distances_b, b_has_cycle = bellman_ford(b)
    
    print(distances_s)
    print(distances_a)
    print(distances_b)
    
    # 3. s->k 까지 합승, k->a & k->b 따로 이동 비용 중 최소값 구하기
    d = float('inf')
    for k in range(1, n+1):
        d = min(d, distances_s.get(k) + distances_a.get(k) + distances_b.get(k))
    
    return d

# # 다익스트라
# def solution(n, s, a, b, fares):
#     answer = 0
    
#     #1. graph 만들기
#     graph = {i : {} for i in range(1,n+1)}
    
#     for c,d,f in fares:
#         if not graph[c].get(d, None):
#             graph[c][d] = f
#         if not graph[d].get(c, None):
#             graph[d][c] = f
    
#     # 2. 다익스트라 함수
#     def dijkstra(start_node):
            
#         #2-1. distances 만들기
#         distances = {i : float('inf') for i in range(1, n+1)}
#         distances[start_node] = 0
    
#         #2-2. 최단거리 찾기
#         queue = []
#         heapq.heappush(queue, [0, start_node])

#         while queue:
#             cur_dist, cur_node = heapq.heappop(queue)

#             if distances[cur_node] < cur_dist:
#                 continue

#             for next_node, weight in graph.get(cur_node).items():
#                 next_dist = cur_dist + weight

#                 if next_dist < distances[next_node]:
#                     distances[next_node] = next_dist
#                     heapq.heappush(queue, [next_dist, next_node])
    
#         return distances
    
#     #2-3. 최단거리 구하기
#     distances_s = dijkstra(s)
#     distances_a = dijkstra(a)
#     distances_b = dijkstra(b)
    
#     # 3. s->k 까지 합승, k->a & k->b 따로 이동 비용 중 최소값 구하기
#     d = float('inf')
#     for k in range(1, n+1):
#         d = min(d, distances_s.get(k) + distances_a.get(k) + distances_b.get(k))
                
#     return d