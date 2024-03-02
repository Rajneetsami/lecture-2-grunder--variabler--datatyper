
Be användaren ange vilken kategori den tillhör-vuxen, pensionär, student. Om den är pensionär eller student kostar resan 20 kr . Om den är vuxen kostar resan 30 kr . Annars skall användaren informeras att den har angett en felaktig kategori.



age_group = input('enter correct age group /vuxen/pensionär/student: ').lower()

if age_group == 'student' or age_group == 'student':
    print('travel cost you 20kr.')
elif age_group == 'vuxen':
    print('travel cost you 30kr.')

else:
    print('invalid entry')
