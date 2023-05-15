n,m = map(int,input().split())
x,y,direction = map(int, input().split())
visit = [[0]*m for _ in range(n)]
visit[x][y] =1
#mat는 방문한 위치 저장
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
#arr 맵의 정보

dx = [-1,0,1,0]
dy = [0,1,0,-1]
#     북 동 남 서(0,1,2,3)으로 주어짐
def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction =3

cnt =1
turn_time = 0
#turn_time이 4가 될 시 네 방향 모두 갈 수 없는 경우를 생각할 수 있음

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if(visit[nx][ny]==0 and arr[nx][ny] ==0 ):
        x= nx; y= ny
        visit[nx][ny] =1
        cnt += 1
        turn_time =0
        continue
    else: #회전한 이후 갈 곳 없으면
        turn_time +=1
    if turn_time == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        if arr[nx][ny]==0:
            x= nx
            y= ny
            turn_time = 0
        else:
            break

print(cnt)



