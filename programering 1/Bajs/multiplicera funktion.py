def mult(a, b):
  # Talen som tas emot kallas parametrar
  the_sum = a * b
  return(the_sum)

x = int(input("vad är första talet? ")) 
y = int(input("vad är andra talet? "))

# Huvudprogram
my_sum = mult(x, y)
print(my_sum)
