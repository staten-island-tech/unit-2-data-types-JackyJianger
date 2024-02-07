
print('How was our service?')
print('Bad(0%), Okay(15%), Good(20%) or Great(25%)')
Service=str(input()).lower()
if (Service == 'bad'):
    global tip_percent
    tip_percent=0
elif (Service == 'okay'):
    tip_percent=15
elif (Service == 'good'):
     tip_percent=20
elif (Service == 'great'):
    tip_percent=25


print('What is your subtotal?')
subtotal=float(input())
def Tip_calculator():
    tip=tip_percent*subtotal/100
    Total=tip+subtotal
    print (Total)
  
Tip_calculator()

