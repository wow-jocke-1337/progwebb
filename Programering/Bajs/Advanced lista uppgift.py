
def game(): 
  try:
    lista = list(range(1,101))

    while True:
      x = int(input("""
  Vad vill du göra?        \n   
  1. Titta på hela listan             2. Titta på en specifik listposition    
  3. Lägga till ett värde i listan    4. Ta bort ett värde i listan 
  5. Sortera listan                   6. Beräkna listans medelvärde
  7. Avsluta

  ---->"""))

      if x == 1:
        print(lista)

      elif x == 2:
        while True:
          z = int(input("vilken position vill du kolla på? -->"))
          if z < 0 or z > 100:
            print("det finns bara 100 tal att välja mellan dumbass")
            z = int(input("vilken position vill du kolla på? -->"))
          print("ok")
          print(lista[z]-1)
          h = (input("vill du kolla på en till position? ja/nej? -->"))
          if h == "nej":
              break
            
      elif x == 3:
        tal = int(input("vad vill du lägga till? -->"))
        print ("ok")
        lista.append(tal)
      elif x == 4:
        tal = int(input("vilken position vill du ta bort? skriv nr  -->"))
        print ("ok")
        lista.pop(tal-1)
      elif x == 5:
        oisjdfois
      elif x == 6:
        iahdoeh
      elif x == 7:
        break

    print("tack för du spelade??")
    spelaigen = (input("Vill du spela igen? ja/nej     ---> "))
    if spelaigen == "ja":
      game()
    else:
      print("ok då :(")

  except ValueError:
    print("för att välja ett alternativ måste du skriva ett heltal o inga bokstäver")
    game()


game()


  