s="swiss"
def First(s):
    for char in s:
        if s.count(char)==1:
            return char
            
print(First(s))