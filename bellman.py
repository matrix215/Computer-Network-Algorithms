import heapq

INF = int(1e9)

n, m = 7,12 # 노드 수, 간선 수 입력 받기
edges = [(1,2,4),(1,3,5),(2,3,6),(2,5,10),(2,4,5),(3,4,4),(3,6,9),(4,5,6),(4,6,3),(5,6,3),(5,7,2),(6,7,2)] # 모든 간선에 대한 정보를 담는 리스트 생성
graph = {
    '1': {'2':4, '3':5},
    '2':{'1':4, '3':6, '4':5},
    '3':{'1':5, '2':6,'6':9, '4':4},
    '4':{'2':5, '3':4, '5':6,'6':3},
    '5':{'2':10, '4':6, '6':3},
    '6':{'5':3, '7':2, '4':3, '3':9},
    '7':{'5':2, '6':2},
}# 길 찾기용

dist = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 그래프 생성
for i in range(m):
    u, v, w = edges[i] # 노드, 인접 노드, 가중치
    edges.append((v, u, w))
print(edges)



# 벨만 포드 알고리즘
def bf(start):

    dist[start]=0 # 시작 노드에 대해서 거리를 0으로 초기화

    for i in range(n): # 정점 수만큼 반복
        for j in range(2*m): # 매 반복 마다 모든 간선 확인
            node = edges[j][0] # 현재 노드 받아오기
            next_node = edges[j][1] # 다음 노드 받아오기
            cost = edges[j][2] # 가중치 받아오기
                # 현재 간선을 거려서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                #print(node,dist[node],'/')


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

# 벨만 포드 알고리즘 수행
for j in range(1,8):
    print ('------노드: ', j,'----------')
    dist = [INF] * (n + 1)

    negative_cycle = bf(j)

    if negative_cycle:
        print('-1')
    else:
        # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
        for i in range(1, n+1):
            if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
                print('무한')
            else: # 도달할 수 있는 겨우 거리를 출력
                str_i=str(i)
                str_j=str(j)
                print('[',j,'->',i,']', 'cost:', dist[i])
                find_dis(graph, str_i, str_j)

