s1=input()
s2=input()
flag=False
if (len(s1)==len(s2)):
    if(set(s1.lower())==set(s2.lower())):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                flag=True
print(flag)              
from collections import Counter
if (Counter(s1)==Counter(s2)):
    print("Anagrams")
else:
    print("Not Anagrams")
