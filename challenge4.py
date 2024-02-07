number1 = int(input('Give me any number'))

i=1
factors1=[]
while i<= number1:
    if number1%i == 0:
        factors1.append(i)
        i+=1
    else:
        i+=1
print(factors1)


number2 = int(input('Give another number'))
a=1
factors2=[]
while a<= number2:
    if number2%a == 0:
        factors2.append(a)
        a+=1
    else:
        a+=1

for factors in factors1:  
    if factors in factors2:
        factors = []     
print(factors2)

