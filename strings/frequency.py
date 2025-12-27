s="Dharani"
res={}
for char in range(5):
    if char not in res:
        res[s]=1
    else:
        res[s]+=1
print(res)