
Jämnt eller udda!
Skriv ett program som gör följande:
• Be användaren om ett heltal < tal >
• Kontrollera om det är udda eller jämnt och skriv ut till användaren vilket det är?
Svårighetsgrad 2
– Kontrollera om talet är delbart med 3 och 5!
– Och om så fallet så skriv ut att:Talet är en multipel av 2 ∗ 3 ∗ 5, d.v.s. det
finns ett tal X så att 2 ∗ 3 ∗ 5 ∗ X =< tal >
Undersök dem aritmetiska operatorerna a%b och a//b




tal = int(input('enter number: '))

if tal%2 == 1:
    if tal%3 == 0 and tal%5 == 0:
     print('tal is multiple of  3 and 5')
     print('talet är udda')
    else:
       print('tal is not multiple of 3 and 5')
       print('talet är udda')
else:
    print('talet är jämn')


   
