
Be användaren mata in sitt födelseår. Om det är större eller lika med 1980 men mindre än 1990 skriv ut –Du är född på 1980-talet. Om det är mindre än 2000 men större än eller lika med 1990 skriv ut- Du är född på 1990-talet. Om det är mindre än 1980 eller större än eller lika med 2000, skriv- Du är inte född på 1990 eller 1980-talen.







birth_year = int(input('enter your birth year: '))

if 1980 <= birth_year <1990:
    print('du är född på 1980 talet')
elif 1990 <= birth_year < 2000:
    print('du är född på 1990 talet')
elif birth_year < 1980 or birth_year >= 2000:
    print('du är inte född på 1990 or 1980 talet')
