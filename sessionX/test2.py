n,k = map(int,input().split())
arr = [1,2,3,4,5]
k=k%n
result = arr[-k:]+arr[:-k]
for num in result:
    print(num,end="")