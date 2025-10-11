amonnt_due=50

while amonnt_due>0:
    print(f'Amont Due {amonnt_due}')
    pyment=int(input('insert coin'))
    if pyment in[25,5,10]:
        amonnt_due-=pyment
    else:
        continue
print(f'change owed {abs(amonnt_due)}')