#반복되는 수열에 대해서 파악 필요
n,m,k=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
max1= arr[n-1]; max2= arr[n-2]
cnt = int((m/(k+1)) * k)
cnt += m %(k+1)
result =0
result += max1 * cnt
result += max2 *(m - cnt)

print(result)
