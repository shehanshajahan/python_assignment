def remove_duplicates(lst):
    res=[]
    for x in lst:
        if x not in res:
            res.append(x)
    return res
list=[1,2,3,3,4,5,5,6,7]
print(remove_duplicates(list))