

Be användaren att mata in hur många paket mjölk som finns kvar. Är det mindre än 10 skriv- Beställ 30 paket. Är det mellan 10 och 20 skriv- Beställ 20 paket. Annars skriv-Du behöver inte beställa någon mjölk.





milk_in_stock = int(input('enter amount: '))

if milk_in_stock < 10:
    print('order 30 packets')
elif 10 <= milk_in_stock < 20:
    print('order 20 packet')
else:
    print('not required')
