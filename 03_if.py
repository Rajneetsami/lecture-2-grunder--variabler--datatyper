
Skriv ett program som gör följande:
Vilken ålder?
• Kontrollera åldern på personen:
• Är (ålder < 13) så skriver vi ut:Personen är ett barn.
• Är (13 <= ålder < 20) så skriver vi ut:Personen är en tonåring.
• Är (67 > ålder >= 20) skriver vi ut:Personen är vuxen.
• Annars är personen (>= 67) och vi skriver då ur:Personen är pensionär. • Och skriv sedan vilket användaren är!




age = int(input('enter yours age: '))

if age < 13:
    print('du är ett barn.')
elif 13 <= age < 20:
    print('du är tonåring')
elif 67 > age >= 20:
    print('du är vuxen')
elif age >= 67:
    print('du är pensionär')
else:
    print('invalid val')
