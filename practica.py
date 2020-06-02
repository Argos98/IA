nom1 = input('nombre 1 ' )
edad = int(input('edad 1 '))
nom2 = input('nombre 2 ') 
edad1 = int(input('edad 2 '))

if edad>edad1:
    print(f'{nom1} es mayor ')
elif edad<edad1:
    print(f'{nom2} es mayor ')
else:
    print('son de la misma edad')