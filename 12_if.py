 Stora if-monstret!
Skriv ett program som gör följande:
• Be användaren skriva in en mening!
• Om användaren inte skrev något utan bara tryckte Enter så skriver vi ut: Jaha, skit i det då! Därefter avslutar vi programmet
• Om användaren skrev in endast mellanslag så skriver vi ut: Spacit!!!
• Om användaren skrev in något som börja med He så ska vi skriva ut: He.........!
• Om användaren skrev in något som slutade med punkt så ska vi skriva ut: Korrekt avslut!
• Om användaren skrev in fler än 24 karaktärer (chars) så ska det skrivas ut: Oj, du va en produktiv jäkel!
• Om det användaren skrev både börja och slutade med samma karaktär så ska vi skriva ut strängen som användaren gav oss utan den första karaktären och utan den sista
• Om det finns 3 stycken a eller 4 stycken b eller 2 c i det användaren skrev in så ska vi skriva ut: aaa eller bbbb eller ccc min kära användare! Notera: Bokstäverna behöver inte vara i rad i meningen!
• Om användaren bara använde stora bokstäver så skriver vi: BIG LETTERS!











text = input('enter en text: ')

if text == '':
    print('jaha, skit i det då!')

if text == ' ':
    print('Spacit!!')

if text.startswith('He'):
    print('He......')

if text.endswith('.'):
    print('Korrekt avsluta')

if len(text) > 24:
    print('Oj, du va en produktiv jäkel!')

if text[0] == text[-1]:
    print(text[1:-1])

if text.count('a') == 3 or text.count('b')== 4 or text.count('c')==2:
    print('aaa eller bbbb eller cc min kära användare')

if text.isupper():
    print('BIG LETTERS') 
