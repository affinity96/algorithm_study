import queue

#상하좌우 탐색해야하니까
dx = [0,-1,0,1]
dy = [-1,0,1,0]

#받아올 리스트
original_list = []

#NM 받아와
N,M = map(int,input().split(' '))

#(n,m)페어된 리스트생
for n in range(N):
    input_string = input()
    for m in range(M):
        number=int(input_string[m])
        if(number)==1 :
            (x,y) = (n,m)
            original_list.append((x,y))
#(0,0)에서부터의 거리를 적어둘 list
distance = [[0 for m_list in range(M)]for n_list in range(N)]
distance[0][0] = 1
#bfs 돌릴 큐
miro_queue = queue.Queue()
#시작점 (0,0) 큐에 들어가
miro_queue.put((0,0))
#방문한 노드 저장하는 리스트
visited = []

#큐가 다 빌때까지 bfs
while miro_queue.empty()==False:
    #큐에서 하나 꺼내
    (a,b) = miro_queue.get()
    #꺼낸 노드 방문했다기록
    visited.append((a,b))
    #상하좌우 모든 노드 탐색
    for i in range(4):
        (a_child, b_child) = (a+dx[i], b+dy[i])
        #옆노드 방문하지 않았다면 방문
        if (a_child, b_child) in original_list and (a_child, b_child) not in visited:
            # 옆노드 큐에 등록하고
            miro_queue.put((a_child,b_child))
            #기존 노드까지의 거리 +1 만큼 옆 노드 길이 갱신
            distance[a_child][b_child] = distance[a][b]+1
#찾고자 하는 노드까지의 거리 출력
print(distance[N-1][M-1])
