x = int(input("Piersze liczbe: "))
y = int(input("Druge liczbe: "))

if x > y:
      x,y = y,x
while x <= y:
    print (x)
    x += 1

