Be användaren mata in två tal.number1 och number2.
Lagra det STÖRSTA talet av dom två i en tredje variabel, largest
Skriv ut:
Det största talet är <>
för tre number



tal1 = int(input('enter one number: '))
tal2 = int(input('enter second number: '))
tal3 = int(input('enter third number: '))


if tal1 >= tal2 and tal1>=tal3:
    tal4 = tal1
elif tal1 <= tal2 < tal3 <= tal2:
    tal4 = tal2
else:
    tal4 = tal3



print('largest number is ', tal4)
