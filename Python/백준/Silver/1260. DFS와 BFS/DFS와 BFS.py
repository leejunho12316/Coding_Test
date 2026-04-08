from collections import deque
import sys
input = sys.stdin.readline

#입력 받기
n,m,v = map(int, input().split())
N,M,start_node=n,m,v

#인접 노드 만들기
adj_node = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_node[a].append(b)
    adj_node[b].append(a)

adj_node = [sorted(l) for l in adj_node]

# print(adj_node)

def DFS(start_node):
    result = ''
    stack = [start_node]
    visited = [False] * (N+1)

    while(stack):
        cur_node = stack.pop(-1)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        result += str(cur_node) + ' '

        #역순으로 방문하지 않은 것 추가
        for i in adj_node[cur_node][::-1]:
            if not visited[i]:
                stack.append(i)

    return result.strip()


def BFS(start_node):
    result = ''
    queue = deque([start_node])
    visited = [False] * (N+1)

    while queue:
        cur_node = queue.popleft()
        visited[cur_node] = True
        result += str(cur_node) + ' '

        for i in adj_node[cur_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result.strip()



dfs_result = DFS(start_node)
bfs_result = BFS(start_node)
print(dfs_result)
print(bfs_result)
