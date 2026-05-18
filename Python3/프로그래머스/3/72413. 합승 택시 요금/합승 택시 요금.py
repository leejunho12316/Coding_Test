import heapq

def solution(n, s, a, b, fares):
    answer = 0
    
    #1. graph 만들기
    graph = {i : {} for i in range(1,n+1)}
    
    for c,d,f in fares:
        if not graph[c].get(d, None):
            graph[c][d] = f
        if not graph[d].get(c, None):
            graph[d][c] = f
    
    # 2. 다익스트라 함수
    def dijkstra(start_node):
            
        #2. distances 만들기
        distances = {i : float('inf') for i in range(1, n+1)}
        distances[start_node] = 0
    
        #3. 최단거리 찾기
        queue = []
        heapq.heappush(queue, [0, start_node])

    
        while queue:
            cur_dist, cur_node = heapq.heappop(queue)

            if distances[cur_node] < cur_dist:
                continue

            for next_node, weight in graph.get(cur_node).items():
                next_dist = cur_dist + weight

                if next_dist < distances[next_node]:
                    distances[next_node] = next_dist
                    heapq.heappush(queue, [next_dist, next_node])
    
        return distances
    
    distances_s = dijkstra(s)
    distances_a = dijkstra(a)
    distances_b = dijkstra(b)
    
    # s->k 까지 합승, k->a & k->b 따로 이동 비용 중 최소값 구하기
    d = float('inf')
    for i in range(1, n+1):

        d = min(d, distances_s.get(i) + distances_a.get(i) + distances_b.get(i))
        
                
    return d