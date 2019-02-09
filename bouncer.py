#Bouncer program

# pede para o usuario entrar com uma idade

age = input('How old are you? ')
if age: #se não estiver em branco...
    age = int(age) # converte a string em um valor inteiro
    if age >= 18 and age <= 21:
        print('You can enter, but need a wristband!')
    elif age >= 21:
        print('You are good to enter and drink!')
    else:
        print('You can´t come in, little one!')
else: # se estiver em branco
    print('Please enter an age!')
    
 
