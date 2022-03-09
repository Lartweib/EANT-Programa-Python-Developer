x = 5 #variable
lista = []
tupla = (3,5,7)

#edades = {'Jorge': 33, 'Ana': 28}
edades = dict(Jorge=33, Ana=28, Lucia=55)

edades['Gonzalo']

for persona in edades:
   print(persona, ':', edades[persona])
   
#Métodos más utilizados
edades.get('Gonzalo', 'Esa persona no está')

edades.update({'Ana': 38})
edades.update(Gonzalo=49)
