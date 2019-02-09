import sys
#Calculadora simples coded by Diego

print('#' * 20)
print('ESCOLHA SUA TABUADA')
print('#' * 20)

print('''
 O script realiza as seguintes operações:
        +                 Somar
        _                 Subtrair
        
        *                 Multiplicar
        
        /                 Divisão (real)
        
        //                Divisão (inteira)
        
''')

escolha = input('Escolha o tipo de operação que deseja realizar: ')
valor_1 = int(input('Valor 1: '))
print()
valor_2 = int(input('Valor 2: '))

if escolha == '+':
    calculo = valor_1 + valor_2
    print('A soma entre {} e {} é: {}'.format(valor_1, valor_2, calculo))
    

elif escolha == '-':
     calculo = valor_1 - valor_2
     print('A subtração entre {} e {} é: {}'.format(valor_1, valor_2, calculo))

elif escolha == '*':
    calculo = valor_1 * valor_2
    print('A multiplicação entre {} e {} é: {}'.format(valor_1, valor_2, calculo))
    
elif escolha == '/':
    calculo = valor_1 / valor_2
    print('A divisão ( do tipo real) entre {} e {} é: {}'.format(valor_1, valor_2, calculo))
    
    
elif escolha == '//':
    calculo = valor_1 // valor_2
    print('A divisão ( do tipo inteira) entre {} e {} é: {}'.format(valor_1, valor_2, calculo))
