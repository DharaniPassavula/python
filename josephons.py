def josephons(n,k):
       
    if n==1:
        return 0
    return (josephons(n-1,k)+k)%n
print(josephons(19,7))