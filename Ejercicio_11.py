#11. Agregue un país que no esté en la lista 
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