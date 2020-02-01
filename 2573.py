#1년후 빙산의 모습을 리턴!
def aYearLater(iceberg,N,M):
    #1년후 빙산 초기화
    next_iceberg = [[0]*M for n in range(N)]
    #동서남북 확인해봐야지
    check_around_list = [[-1,0],[0,-1],[1,0],[0,1]]
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] >0:
                #동서남북중 몇개에 0있나 (얼마만큼빼야하나) 카운트
                down_count = 0
                for change in check_around_list:
                    a = x+change[0]
                    b = y+change[1]
                    #범위 밖이면 pass
                    if a<0 or b<0 or a>=N or b>=M:
                        continue
                    else :
                        #주변에 0이있을때마다 count++
                        if iceberg[a][b] == 0: down_count +=1
                next_iceberg[x][y] =iceberg[x][y]- down_count
                #0보다 작으면 걍 0
                if next_iceberg[x][y] < 0 : next_iceberg[x][y] = 0

    return next_iceberg

#부셔졌나? 확인하는 DFS함수
def isBreaked(iceberg,N,M):
    color = [[0]*M for n in range(N)]
    #뭉탱이(2개이상이면 부셔졌겠지)
    moong = 0
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] !=0:
                #0이아닌(얼음이있는)모든 노드를 1로 초기화. 0으로 해버리면 물인 곳과 비교가안댐
                color[x][y] = 1
    for x in range(N):
        for y in range(M):
            #옆에도 빙산이있다면?            
            if color[x][y]==1:
                #재귀
                isBreaked_visit(iceberg,x,y,color,N,M)
                #이 루프가 끝나면 한 뭉탱이가 생성되겠지
                moong+=1
    return moong


def isBreaked_visit(iceberg,x,y,color,N,M):
    check_around_list = [[-1,0],[0,-1],[1,0],[0,1]]
    #일단 컬러를 2로 바꿔(첫방문)
    color[x][y] = 2
    #마찬가지로 동서남북 탐방 후 있다면 방문
    for check in check_around_list:
        a = x+check[0]
        b = y+check[1]
        if a<0 or b<0 or a>=N or b>=M: continue
        else:
            if color[a][b] == 1: isBreaked_visit(iceberg, a,b, color,N,M)
    #다 방문했으면 컬러를 3으로 (두번째방문(거꾸로방문))
    color[x][y] = 3

    


def main():

    N, M = map(int, input().split(' '))
    original_iceberg= []
    for n in range(N):
        original_num_list = list(map(int,input().split(' ')))
        original_iceberg.append(original_num_list)
    
    answer = 0
    #첫 뭉탱이 
    moong = isBreaked(original_iceberg,N,M)
  
    #뭉탱이가 1이 아니면 그만해야댐(2가 되는 순간 갈라지니까)
    while moong == 1:
        #한 해가 지나갑니다
        next_iceberg = aYearLater(original_iceberg,N,M) 
        answer += 1
        #몇개의 뭉탱이가 생겼을까요
        moong = isBreaked(next_iceberg,N,M)
        original_iceberg = next_iceberg

    print(answer)

if __name__ == '__main__':
    main()
