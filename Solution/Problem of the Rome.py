T=int(input())
sym=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
while T:
    num=int(input())
    if num>3999:
        print("Invalid input")
        break
    res=""
    i=0
    while i<13 and num>0:
        while num >=val[i]:
            div=num//val[i]
            num-=div*val[i]
            while div:
                res+=sym[i]
                div-=1
        i+=1
    print(res)
    T-=1