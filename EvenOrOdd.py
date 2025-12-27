s=[1,2,5,3,6,0,1,2,2]
even=[]
odd=[]
def EvenorOdd(num):
    if num % 2==0:
        even.append(num)
    else:
        odd.append(num)
for num in s:
    EvenorOdd(num)
print(even)
print(odd)