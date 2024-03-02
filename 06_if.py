
Vokal eller konsonant!
Skriv ett program som gör följande:
• Frågar användaren om en karaktär. D.v.s. en char
• Avgör om det är en volka eller inte och skriv ut svaret till användaren!
Kom ihåg att det finns en in operator i Python!





char = input('enter en char: ').lower()
vokal = ['a','e','i','o','u','ä','å','ö'] 

if char in vokal:
    print('vokal char')
else:
    print('inte vokal char')
