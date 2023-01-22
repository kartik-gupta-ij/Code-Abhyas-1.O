n=int(input())
A=[]
A.append(n)
while n!=1:
    if n%2 ==0:
        n=n//2
        A.append(n)
    else:
        n=(n*3)+1
        A.append(n)
for i in range(len(A)):
    print(A[i],end=" ")