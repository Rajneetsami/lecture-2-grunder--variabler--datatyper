


Temperaturer!
Skriv ett program som gör följande:
• Fråga användaren om temperaturen ute! Celsius ! (float)
• Är temperaturen mindre än noll så skriv ut:Det är jättekallt ute!
• Är temperaturen noll eller 10 eller någon temperatur där emellan så ska det skrivas ut: Det är rätt så kallt ute!
• Är temperaturen mer än tio men mindre eller lika med 20 så ska vi skriva ut:Vi kanske överlever!
• Annars så skriver vi ut:Nästan som att vi kan ju tro att det är sommar!








temp = int(input('enter outside temp: '))

if temp < 0:
    print('det är jätte kallt ute')
elif 0 < temp<=10:
    print('det är rätt så kallt ute')
elif 10 < temp <=20:
    print('vi kanske overlever')
else:
    print('det är sommar')
