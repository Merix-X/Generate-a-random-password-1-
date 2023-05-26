from random import randrange, choice
import win32clipboard

def vypis_znaky():
  znaky = ":><?@#$%^&*()_+-=[]{}|;':\",./<>\\"
  neco3 = choice(znaky)
  return neco3
  
def pismeno_a_cislo():
  abeceda = "ABCDEFGHCHIJKLMNOPQRSTUVWXYZabcdefgjklmnopqrstuvwxyz012345689"
  neco = choice(abeceda)
  return neco
  
def kombinace(E=int):
  print("The special characters are as follows:     ><?@#$%^&*:()_+-=[]{}|;':/\",.<>")
  A2 = int(input("How many special characters do you want to use in your password?: "))
  print()
  retezec3 = []
  znaky2 = []
  for x in range(A2):
      znak1 = vypis_znaky()
      znaky2.append(znak1)

  for w in range(E):
      string1 = pismeno_a_cislo()
      retezec3.append(string1)

  for y in range(A2):
      retezec3.pop()

  pocitadlo1 = 0
  for z in range(A2):
      B1 = randrange(1, E+1)
      B1 = B1-1
      zn1 = znaky2[pocitadlo1]
      retezec3.insert(B1, zn1)
      pocitadlo1 = pocitadlo1+1
  retezec4 = ""
  rete1 = retezec4.join(retezec3)
  print(rete1)
  return rete1






D = int(input("How long do you want your password to be?: "))
heslo5 = kombinace(D)
print()
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(heslo5)
win32clipboard.CloseClipboard()
print("Your password has been copied into windows clipboard, use it with Ctrl+v key combination", end="\n\n")
enter = input("--> Press enter to exit <--")
