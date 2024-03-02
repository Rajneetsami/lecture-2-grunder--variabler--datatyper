 Skandinavien
Skriv ett program som gör följande:
Be användaren skriva in ett land!
• Kontrollera om användaren skrev in ett skandinaviskt land, om så fallet så ska det skrivas ut: Det landet tillhör Skandinavien!
Lite klurigare
– Använd endast en if sats! Ännu klurigare
– Använd endast en if sats och in operatorn




country = input('enter your country of living: ').lower()

if country in ['sverige', 'denmark','norge', 'finland']:
    print('you are living in scandniavian country')
else:
    print('you are not living in scandanivian country.')
