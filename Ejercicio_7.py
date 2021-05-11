#7. Busque e imprima la Capiltal de Colombia
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