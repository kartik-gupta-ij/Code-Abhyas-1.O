T=int(input())
while T:
    N,K=map(int,input().split())
    A=[]
    A=(input().split())
    count=0
    for i in range(len(A)):
        code = int(A[i])+K
        if code%7==0:
            count+=1
    print(count)
    T-=1