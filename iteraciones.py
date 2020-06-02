#este es un while normal 
cont = 0 

while cont <10:
    print(cont)
    cont +=1

#este es un while dentro de otro
print('\n')


cont = 0
contInt = 0

while cont < 5:
    while contInt<6:
        print(cont, contInt)
        contInt +=1

    cont +=1
    contInt = 0   


