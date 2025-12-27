s="ate"
r="tae"
def anagram(s,r):
    if len(s)!=len(r):
        return False
    for char in s:
        if char not in r:
            return False
        return True
print(anagram(s,r))