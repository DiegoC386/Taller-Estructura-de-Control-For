archivo = open('paises.txt', 'r')
""""
for pais_y_capital in archivo:
  print(pais_y_capital)
"""
#1. Cuente e imprima cuantas ciudades inician con la letra M
"""
archivo = open('paises.txt', 'r')
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
	if(i[0]=="M"):
		print(i)
		lista.append(i)
		print(len(lista))
archivo.close()
"""
#2. Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
archivo = open('paises.txt', 'r')
print("Paises con inicial con la Letra U: ")
lista1=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista1.append(i[r])
  a="".join(lista1)
  paises.append(a)
  lista1=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
print("Capital con inicial con la Letra U: ")
print()
archivo = open('paises.txt', 'r')
lista2=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista2.append(i[r])
  a="".join(lista2)
  ciudad.append(a)
  lista2=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i)
archivo.close()
"""
#3. Cuente e imprima cuantos paises que hay en el archivo
"""
archivo = open('paises.txt', 'r')
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1
print(len(lista))
archivo.close()
"""
#4. Busque e imprima la ciudad de Singapur
"""
archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
b=a.index(":")
lista2=[] 
for i in range(0,b):
      lista2.append(a[i])  
      unir="".join(lista2)
print(unir)
archivo.close()
"""
#5. Busque e imprima el pais de Venezuela y su capital
"""
archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)
archivo.close()
"""
#6. Cuente e imprima las ciudades que su pais inicie con la letra E
"""
archivo = open('paises.txt', 'r')
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    print(i)
    lista.append(i)
    print(len(lista))
archivo.close()
"""
#7. Buesque e imprima la Capiltal de Colombia
"""
archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
b=a.index(":")
tamaño=len(a)
lista2=[] 
for i in range(b,tamaño):
      lista2.append(a[i])  
      unir="".join(lista2)
print("La Capital de Colombia es: "+str(unir))
archivo.close()
"""
#8. imprima la posicion del pais de Uganda
"""
archivo = open('paises.txt', 'r')
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
archivo.close()
"""
#9. imprima la posicion del pais de Mexico
"""
archivo = open('paises.txt', 'r')
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
x=paises.index("México")+1
print(x)
archivo.close()
"""
#10. El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean
#para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien
#es Antananarivo, espero que el alcalde se vaya contento por su trabajo.
#Utilice un For para cambiar ese Dato
"""
with open('paise.txt') as archivo:
  lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
  lista=[]   
b=a.index(":")
tamaño=len(a)
lista2=[] 
for i in range(0,tamaño):
      lista2.append(a[i])
lista2.remove("b")
2==("Antananarivo")
lista2.insert(1,2)
print(lista2)
archivo.close()
"""
#11. Agregue un país que no esté en la lista
"""
archivo = open('paises.txt', 'r')
P=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  P=P+1 
  if(a=="Paises\n"):
    break
b=a.index(":")
tamaño=len(a)
lista2=[] 
for i in range(0,tamaño):
      lista2.append(a[i])
lista2.insert(0,"Nabacasgar: Endananariva\n")
unir="".join(lista2)
print(unir)
archivo.close()
"""