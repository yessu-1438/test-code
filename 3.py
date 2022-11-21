def rotatedDigits(n):
    l=[]
    count = 0
    for i in range(0,10000):
        nSet = set(list(str(i)))
        if (not nSet.intersection({'3','4','7'}) and 
                nSet.intersection({'1','0','2','5','6','8','9'})):
            l.append(i)  
    return l[n]
n=int(input())
print(rotatedDigits(n))