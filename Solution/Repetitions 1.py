x=int(input())
print(x,end=' ')
def al(i):
    if(i%2==1):
        if(i!=1):
            print(i*3+1,end=' ')
            al(i*3+1)
    else:
        print(i//2,end=' ')
        al(i//2)
al(x)