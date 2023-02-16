def funktion():
    try:
      tal1 = int(input("Skriv in täljaren --> "))
      tal2 = int(input("Skriv in nämnaren --> "))
      print(tal1/tal2)
    except ValueError:
        print("Du måste skriva ett heltal, utan bokstäver")
    except ZeroDivisionError:
        print("Du får inte skriva in 0 ")
    
funktion()
