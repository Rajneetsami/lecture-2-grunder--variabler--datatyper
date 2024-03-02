print(type(7))
print(type(4.5))
print(type('rajneet'))
print(type(10)==type(42))#kontroller om type är likdana
print(isinstance(1,int))#returns True if the specified object is of the specified type, otherwise False
print(isinstance(1, float))
print(type(type))
print(f"{type(5)=}")#f sträng 
print(f"{type(5.7)=}")
print(f"{type('sträng')=}")
print(f"{type(None)=}")
print(f"{type(False)=}")
print(f"{type(True)=}")
print(f"{type('s')=}")#f string hjälper i formatter  text
#stränger deklarer med enkel fnuttar, dobel fnuttar och tripel fnuttar
print("""dokumentra
      vad vårat
      program gör!""")
var = 42
fstring =f'jag vill ha en ny rad {var +10}'
print(fstring)