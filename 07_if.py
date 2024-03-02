
Palindrom!
Skriv ett program som gör följande:
• Be användaren skriva in ett ord!
• Avgör om ordet är ett palindrom (ord som läses likadant framifrån och bakifrån) Exempel: rappar
Använd slicing och vänd på ordet! Skriv sedan om det är ett palindrom eller inte!






ord = input('enter one word: ')

if ord == ord[::-1]:
    print('ord is palindrom')
else:
    print('inte palindrom')
