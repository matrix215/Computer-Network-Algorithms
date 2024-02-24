import heapq
INF = int(1e9)

n,m=7,12
# 2차원 거리테이블 리스트 초기화
edges = [(1, 2, 4), (1, 3, 5), (2, 3, 6), (2, 5, 10), (2, 4, 5), (3, 4, 4), (3, 6, 9), (4, 5, 6), (4, 6, 3), (5, 6, 3),(5, 7, 2), (6, 7, 2)]
#길 찾기용 그래프
graph_for_find_path = {
    '1': {'2':4, '3':5},
    '2':{'1':4, '3':6, '4':5},
    '3':{'1':5, '2':6,'6':9, '4':4},
    '4':{'2':5, '3':4, '5':6,'6':3},
    '5':{'2':10, '4':6, '6':3},
    '6':{'5':3, '7':2, '4':3, '3':9},
    '7':{'5':2, '6':2},
}

graph = [[INF] * (n+1) for _ in range(n+1)]
# 자신의 노드간의 거리는 0으로 변경

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 주어지는 그래프 정보 입력
for _ in range(m):
    # a -> b로 가는 비용은 c
    a, b, c = edges[_]
    graph[a][b] = c
    graph[b][a] = c

# k=거쳐가는 노드
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#길찾기 알고리즘
#우선 순위 큐를 이용하여 만들었다
def find_dis(graph, first, last):
    distance = {node:[float('inf'), first] for node in graph}
    distance[first] = [0, first]
    queue = []
    # 시작 노드부터 탐색 시작 하기 위함. (거리, 노드) - 거리, 노드 순으로 넣은 이유는 heapq 모듈에 첫 번째 데이터를 기준으로 정렬을 진행하기 때문
    # (노드, 거리) 순으로 넣으면 최소 힙이 예상한대로 정렬되지 않음

    heapq.heappush(queue, [distance[first][0], first])
    # 우선 순위 큐에 데이터가 하나도 없을 때까지 반복
    while queue:
        # 가장 낮은 거리를 가진 노드와 거리를 추출
        current_distance, current_node = heapq.heappop(queue)
        # 이미 처리된 노드라면 무시# 파이썬 heapq에 (거리, 노드) 순으로 넣다 보니까 동일한 노드라도 큐에 저장이 된다 예시: queue[(7, 'B'), (10, 'B')]
        # 이러한 문제를 아래 조건문으로 이미 계산되어 저장한 거리와 추출된 거리와 비교하여 저장된 거리가 더 작다면 비교하지 않고 큐의 다음 데이터로 넘어간다.
        if distance[current_node][0] < current_distance:
            continue
        # 대상인 노드에서 인접한 노드와 거리를 순회
        for next_node, weight in graph[current_node].items():
            # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함
            total_distance = current_distance + weight
            # 배열의 저장된 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경
            if total_distance < distance[next_node][0]:
                # 다음 노드까지 총 거리와 어떤 노드를 통해서 왔는지 입력
                distance[next_node] = [total_distance, current_node]
                # 다음 인접 거리를 계산 하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)
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


for i in range(1, n+1):
    print('-------노드',i,'--------')
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('무한')
        else:
            str_i = str(i)
            str_j = str(j)
            print('[', i, '->', j, ']', 'cost:', graph[i][j])
            find_dis(graph_for_find_path, str_j, str_i)