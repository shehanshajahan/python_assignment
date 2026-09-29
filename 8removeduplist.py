arr=list(map(int,input().split()))

seen=set()
res=[]

for x in arr:
    if x not in seen:
        res.append(x)
        
    seen.add(x)
print(res)