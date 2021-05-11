#4. Busque e Imprima la ciudad de Singapur
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