
print('Type your subtotal here:')
subtotal=float(input())

def Tip_calculator(tip_percent):
    tip=tip_percent*subtotal/100
    Total=tip+subtotal
    print (Total)
    
Tip_calculator(15)


