n = int (input("Podaj liczbstudentów"))

i = 1
suma = 0

while i < n+1:
    punkty = float (input(f"Podaj liczbę punktów srudrnta {i} : "))
    if  punkty < 0 or punkty > 100:
        continue
    i = i + 1
    suma = suma + punkty


srednia = suma / n
    print (f"srednia wynosi: {srednia}")