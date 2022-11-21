def sol(n):
    si = '-' if n<0 else ''
    n = abs(n)
    if n < 3:
        return str(n)
    s = ''
    while n != 0:
        s = str(n%3) + s
        n = n//3
    return si+s
n=int(input())
print(sol(n))