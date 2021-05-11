#9. Imprima la posicion del Pais de Mexico
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