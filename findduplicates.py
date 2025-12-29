s=[1,4,2,5,4,9,2,5,8,1,8]
res=[]
freq={}
for num in s:
    freq[num]=freq.get(num,0)+1
for val in freq:
    if freq[val]>1:
        res.append(val)
print(res)
    