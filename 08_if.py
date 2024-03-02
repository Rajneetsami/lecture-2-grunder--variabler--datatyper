


Omkretsen
Skriv ett program som gör följande:
• Fråga användaren om en radie för en cirkel!
• Beräkna omkretsen. Om omkretsen är större än 50, skriv ut Stor cirkel”, annars Liten cirkel”.
Omkrets beräknas genom 2 · π · radie PS: pythons math-modul





import math

radius = int(input('enter radius of circle: '))
area = 2*math.pi*radius

if area > 50:
    print('circle is large')
else:
    print('liten circle')
