import heapq
INF = int(1e9)

n, m = 7,12 # 노드 수, 간선 수 입력 받기
edges = [(1, 2, 4), (1, 3, 5), (2, 3, 6), (2, 5, 10), (2, 4, 5), (3, 4, 4), (3, 6, 9), (4, 5, 6), (4, 6, 3), (5, 6, 3),(5, 7, 2), (6, 7, 2)]
graph_for_find_path = {
    '1': {'2':4, '3':5},
    '2':{'1':4, '3':6, '4':5},
    '3':{'1':5, '2':6,'6':9, '4':4},
    '4':{'2':5, '3':4, '5':6,'6':3},
    '5':{'2':10, '4':6, '6':3},
    '6':{'5':3, '7':2, '4':3, '3':9},
    '7':{'5':2, '6':2},
}# 길 찾기용
graph = [[] for _ in range(n + 1)]
# 모든 간선에 대한 정보를 담는 리스트 생성

#distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화


#start = int(input())
# 주어지는 그래프 정보 담는 N개 길이의 리스트
#graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)  # 방문처리 기록용
distance = [INF] * (n+1)   # 거리 테이블용

for _ in range(m):
    a, b, c = edges[_]
    graph[a].append((b, c))
    graph[b].append((a, c))

print(graph)
# 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작노드 -> 시작노드 거리 계산 및 방문처리
    distance[start] = 0
    visited[start] = True
    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_smallest_node()  # 방문X 면서 시작노드와 최단거리인 노드 반환
        visited[now] = True        # 해당 노드 방문처리
        # 해당 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            cost = distance[now] + next[1]  # 시작->now 거리 + now->now의 인접노드 거리
            if cost < distance[next[0]]:    # cost < 시작->now의 인접노드 다이렉트 거리
                distance[next[0]] = cost

def find_dis(graph, first, last):
    distance = {node:[float('inf'), first] for node in graph}
    distance[first] = [0, first]
    queue = []

    heapq.heappush(queue, [distance[first][0], first])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node][0] < current_distance:
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node][0]:
                # 다음 노드까지 총 거리와 어떤 노드를 통해서 왔는지 입력
                distance[next_node] = [total_distance, current_node]
                heapq.heappush(queue, [total_distance, next_node])
    # 마지막 노드부터 첫번째 노드까지 순서대로 출력
    path = last
    path_output = last + '->'
    while distance[path][1] != first:
        path_output += distance[path][1] + '->'
        path = distance[path][1]
    path_output += first
    print(path_output)
    return distance


for j in range(1,8):
    visited = [False] * (n + 1)  # 방문처리 기록용
    distance = [INF] * (n + 1)  # 거리 테이블용
    dijkstra(j)
    print('------노드',j,'---------')
    for i in range(1, n+1):
        if distance[i] == INF:
            print('무한')
        else:
            str_i = str(i)
            str_j = str(j)
            print('[',j,'->',i,']', 'cost:', distance[i])
            find_dis(graph_for_find_path, str_i, str_j)