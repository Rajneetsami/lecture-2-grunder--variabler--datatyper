# Vi ska skriva ett program (konsolapplikation) som frågar användaren om:
# Namn
# Ålder
# Antal djur som den äger
# Adress
# Bruttolön

# Programmet ska sedan skriva ut:
# Hej på dig <Namn>
# Du är <Ålder> och om 10 år kommer du vara <ålder + 10>
# Att du har djur är <True, False>
# Du bor på <Adress>
# Och efter skatt tjänar du <Bruttolön * 0.31>

namn = input('skriv ditt namn: ' )
age = int(input('skriv din ålder: '))
antal_djur = int(input('anta djur du har: '))
adress =  input('skriv in din adress:' )
lön = int(input('skriv din lön: '))

print(f'Hej på dig {namn}')
print(f'Du är ålder {age} och om 10 år kommer du vara {age + 10}')
print('Du är {} och om 10 år kommer du vara {}'.format(age, age+10))
print(f' du bor på {adress}')
print(f'och efter skatt tjänar du {lön*0.69}')