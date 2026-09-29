arr=list(map(int,input().split()))
largest=float('-inf')
secondl=float('-inf')

for i in range(len(arr)):
    if arr[i]>largest:
        secondl=largest
        largest=arr[i]
    elif arr[i]>secondl and arr[i]!=largest:
        secondl=arr[i]
print(secondl)