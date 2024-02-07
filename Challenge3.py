number = int(input('Give me any number'))

i=1
factors=[]
while i<= number:
    if number%i == 0:
        factors.append(i)
        i+=1
    else:
        i+=1

print(factors)
