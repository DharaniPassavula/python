s="studying"
vowel_count=0
cons_count=0
vowels=['a','e','i','o','u']
for i in range(len(s)):
    if s[i] in vowels:
        vowel_count+=1
    else:
        cons_count+=1
print(vowel_count)
print(cons_count)