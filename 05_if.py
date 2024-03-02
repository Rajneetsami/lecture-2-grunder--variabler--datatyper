
Skottår!
Skriv ett program som gör följande:
• Be användaren om ett årtal!
• Om det är ett skottår så ska vi skriva ut:Det är skottår, det bör vi fira!
• Annars skriver vi ut:Tusan också att det inte är skottår då!
Skottår, följ länken och läs om den Gregorianska Kallendern!


year = int(input('enter year: '))

if year%4 == 0:
    print('det är ett skottår')
else:
    print('inte')
