import random as rand

def spela():
  # Här skriver du funktionen...
  # ...och returnerar antalet försök
  z = 0
  x = rand.randint(1,10)
  while True:
    y = int(input("Gissa talet biatch --->"))
    if y == x:
      z = z + 1
      return(z)
      break
    elif y < 0 or y > 10:
      print("du måste gissa mellan 1 o 10 dumbass bitch")
    else:
      z = z + 1

# Huvudprogram
antal_försök = spela()
print(f"Du klarade det på {antal_försök} försök biaaatchh")

