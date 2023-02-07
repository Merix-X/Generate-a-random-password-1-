from random import randrange, choice
import array
  
def vypis_znaky():
  znaky = ":><?@#$%^&*()_+-=[]{}|;':\",./<>\\"
  neco3 = choice(znaky)
  return neco3
  
def pismeno_a_cislo():
  abeceda = "ABCDEFGHCHIJKLMNOPQRSTUVWXYZabcdefgjklmnopqrstuvwxyz012345689"
  neco = choice(abeceda)
  return neco
  
def kombinace(E=int):
  znaky1 = int(input("Kolik netypických znaků, chceš použít v hesle?: "))
  
  znaky = [znaky1]
  for x in range(znaky1):
    if x == 0:
      znak = vypis_znaky()
      znaky.append(znak)
    #else:
      #for w in range(znaky.count):
        

  for y in range(E):
    nahoda = randrange(1, E)
    if y == 0:
      retezec = pismeno_a_cislo()
    else:
      retezec = retezec[:nahoda] + pismeno_a_cislo() + retezec[nahoda:]
  print(retezec)



D = int(input("Jak dlouhé chceš mít heslo? Už vestavěná délka hesla je 9 znaků!: "))
kombinace(D)