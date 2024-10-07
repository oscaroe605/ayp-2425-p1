direcciones = input("indique la direccion en la que se desea mover: ")
igual_x = 0
igual_y = 0
y = 0
lista_y = [0]
x = 0
lista_x = [0]
for i in direcciones:
    if i == "N" or i == "n":
        y += 1
        lista_y.append (y)
    elif i == "S" or i == "s":
        y -= 1
        lista_y.append (y)
    elif i == "E" or i == "e":
        x += 1
        lista_x.append (x)
    elif i == "W" or i == "w":
        x -= 1
        lista_x.append (x)
    else:
        print ("Por favor introduzca una direccion aceptable") 
for j in lista_x:
    for k in lista_x:
        if j == k:
            igual_x += 1
for l in lista_y:
    for m in lista_y:
        if l == m:
            igual_y += 1
if igual_x > len(direcciones) and igual_y > len(direcciones) :
    print("True")
else:
    print("False")
