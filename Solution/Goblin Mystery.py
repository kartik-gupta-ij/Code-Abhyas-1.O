t=int(input())
for a in range(t):
    x,y=map(int,input().split())
    z=list(input().split())
    c=0
    for i in range(x):
        z[i]=int(z[i])+y
        if z[i]%7==0:
            c+=1
    print(c)