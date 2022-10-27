x = int(input("Piersze liczbe: "))
y = int(input("Druge liczbe: "))

if x > y:
      x,y = y,x
while x <= y:
    if  x%2 == 1:
        x = x+1
        continue

    print (x)
    x += 1