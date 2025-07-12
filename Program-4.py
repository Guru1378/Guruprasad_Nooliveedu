def dictionary(listt):
    dicii={i:0 for i in range(1,10)}
    if not listt:
        return {}
    for i in range (1,10):
        for num in listt:
            if num%i==0:
                dicii[i]+=1
    return dicii
listt=list(map(int,(input("Enter a number: ")).split(",")))
result=dictionary(listt)
print(result)
                
        