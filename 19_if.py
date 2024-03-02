


Be användaren att mata in namnet på ett land där den bor. Om det är Sverige, Danmark, eller Norge skall användare informeras att-Du bor i Skandinavien. Om inte meddela användaren att den inte bor i Skandinavien.








country = input('enter your country of living: ').lower()

if country in ['sverige', 'denmark','norge']:
    print('you are living in scandniavian country')
else:
    print('you are not living in scandanivian country.')
