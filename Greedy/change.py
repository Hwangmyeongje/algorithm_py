# 거슬러줘야 할 동전의 최소 개수
n = int(input())
cnt = 0
coin =[500,100,50,10]
for i in coin:
    cnt += n // i
    n %= i
print(cnt)
