
Största talet?
Skriv ett program som gör följande:
• Frågar användaren om tre tal! Kan va float. Anta att användaren skriver in korrekt!
• Avgör vilket tal som är störst! Är det de första talet skriver vi ut:Det första talet är störst. Om det är det andra talet skriver vi ut:Det andra talet är störst.



tal1 = float(input('enter first float tal: '))
tal2 = float(input('enter second float tal: '))
tal3 = float(input('enter third float tal: '))

if tal1 >= tal2 and tal1 >= tal3:
    print(f'first float number {tal1} is largest')
elif tal2 >= tal1 and tal2 >= tal3:
    print(f'second float number {tal2} is largest')
else:
    print(f'third float number {tal3} is largest')
