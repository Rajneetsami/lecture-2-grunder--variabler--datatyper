
Be användaren mata in två tal.number1 och number2.
Lagra det STÖRSTA talet av dom två i en tredje variabel, largest
Skriv ut:
Det största talet är <>


tal1 = int(input('enter one number: '))
tal2 = int(input('enter second number: '))


if tal1 >= tal2:
    tal3 = tal1
else:
    tal3 = tal2

print('largest number is ', tal3)
