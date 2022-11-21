s1=input()
s2=input()
l=list(s1)
c=0
n=s2[len(s2)-1]
for i in l:
    if n in i:
        c+=1
print(c)