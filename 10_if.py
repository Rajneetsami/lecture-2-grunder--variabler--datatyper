



Priset
Skriv ett program som gör följande:
 2.11
• Frågar användaren om ett pris
• Om varan kostar mer än 1000kr så ska en 10% rabbat appliceras på priset! Skriv ut det totala priset!
pris = int(input('enter price: '))

if pris > 1000:
    print('då för du rabbat 10 %')
    total_priset = (pris - (pris*.1))
    print(total_priset)
else:
    print('du betalar normal prist')
