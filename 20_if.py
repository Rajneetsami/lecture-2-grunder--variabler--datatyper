Be användaren mata in en summa på hur mycket pengar den har. Be sedan användaren att ange om den har rabatt.
stefan.holmberg@systementor.se
0760 - 21 42 21
https://education.systementor.se
  a. Om summan är mellan 15 och 25 och användaren inte har rabatt skriv – Du kan köpa en liten hamburgare.
b. Om summan är mellan 15 och 25 och användaren har rabatt skriv – Du kan köpa en liten hamburgare och en pommes frites.
c. Om summan är större än 25 och mindre än eller lika med 50 och användaren inte har rabatt skriv – Du kan köpa en stor hamburgare.
d. Om summan är större än 25 och mindre än eller lika med 50 och användaren har rabatt skriv – Du kan köpa en stor hamburgare och pommes frites.
e. Om summan är större än 60 eller om den är 50 och 60 och användaren har rabatt skriv – Du kan köpa ett meal med dryck
sum = int(input('enter sum: '))
rabbat = input('enter if you have discount yes/no: ').lower()

if (15 < sum <= 25) and rabbat == 'no':
    print('du kan köpa liten hamburgare')

elif (15 < sum <= 25) and rabbat == 'yes':
    print('du kan köpa liten hamburgare and lien pommes')
elif (25 < sum <= 50) and rabbat == 'no':
    print('du kan köpa en stor hamburgare')
elif (25 < sum <= 50) and rabbat == 'yes':
    print('du kan köpa stora hamburagre and pommes')
elif  (sum > 60) or (50 < sum <= 60) and rabbat == 'yes':
    print('du kan köpa ett meal med drycka')

else:
    print('you dont have tillräckligt sum')
