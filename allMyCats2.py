cat_names = [] #cria uma lista vazia
while True: #enquanto for verdade repetir 
    name = input('Enter the name of cat' + str(len(cat_names) +  1) + ' (or enter nothing to stop)')
    if name == '':
        break
    cat_names = cat_names + [name] #concatena a lista
    print('The cat names are:')
    for name in cat_names:
        print(' ' + name)