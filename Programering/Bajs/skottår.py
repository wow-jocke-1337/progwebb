år = int(input("Vilket årtal? ")) 
skottår=år%4
skottårr=år%100
skottårrr=år%400

if skottår == 0:
    print("det är ett skottår")
elif skottårr == 0:
    print("det är ett skottår")
elif skottårrr == 0:
    print("det är ett skottår")

else: print("det är inte ett skottår")
