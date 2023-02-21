import random as rand 
lista = list(range(1, 36)) 
urna = []
for i in range (7):
  random = rand.randint(0, len(lista)-1)
  urna.append(lista.pop(random))
print(sorted(urna))