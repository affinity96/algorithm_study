# queue로 하면 not in temp_queue 안되길래 이걸로함
from collections import deque

N,K = map(int, input().split(' '))

#bfs할때 쓸 큐
temp_queue = deque()
#시작지점 설정
temp_queue.append(N)
#빙문한 노드
visited = [ 0 for i in range(100001)]
#각 노드마다 시간을 기록하기위한 리스트
time = [ 0 for i in range(100001)]
flag = 0
# 큐가 비거나, k를 만날경우 종료
while temp_queue and flag==0:
    #큐에서 하나 뽑고
    current_num = temp_queue.popleft()
    #그 노드 방문했다 기록
    visited[current_num] = 1
    # 해당 노드의 +1, -1, *2 번의 노드들 탐색
    for next_num in [current_num-1, current_num+1, current_num*2]:
        # 범위 벗어나지 않고, 큐에 없으며, 방문하지 않았을 경우에
        if 0<=next_num<=100000 and next_num not in temp_queue and visited[next_num]==0:
            #큐에 넣고 시간 +1
            temp_queue.append(next_num)
            time[next_num] = time[current_num]+1
            if next_num == K :
                flag = 1
                break

print(time[K])
