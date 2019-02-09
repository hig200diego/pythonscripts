import random

print('#' * 50)
print()
print('START GAME ' * 4)
print()
print('#' * 50)

options = ['rock', 'paper', 'scissors']
            #0         1          2
    
while True:
    p1 = input('Player1 choice: ')
    
    no_cheating = ('#NO CHEATING#')
    
    for i in range(40):
        print(no_cheating)
    
    p2 = random.choice(options)
    
    if p1 and p2 in options:
        print('SHOOT!')
        break
    else:
        print('SOMETHING WENT WRONG')

if p1 == options[0]:
    if p2 == options[1]:
        print('Computer WINS!')
    elif p2 == options[2]:
        print('Player1 WINS!')
    elif p1 == options[0] and p2 == options[0]:
        print('It´s a tie!')
    
elif p1 == options[1]:
    if p2 == options[0]:
        print('Player1 WINS!')
    elif p2 == options[2]:
        print('Computer WINS!')
    elif p1 == options[1] and p2 == options[1]:
        print('It´s a tie!')
   
elif p1 == options[2]:
    if p2 == options[0]:
        print('Computer WINS!')
    elif p2 == options[1]:
        print('Player1 WINS!')
    elif p1 == options[2] and p2 == options[2]:
        print('It´s a tie!')
    
    
elif p2 == options[0]:
    if p1 == options[1]:
        print('Player1 WINS!')
    elif p2 == options[2]:
        print('Computer WINS!')
    elif p2 == options[0] and p1 == options[0]:
        print('It´s a tie!')
        
elif p2 == options[1]:
    if p1 == options[0]:
        print('Computer WINS!')
    elif p1 == options[2]:
        print('Player1 WINS!')
    elif p1 == options[1] and p2 == options[1]:
        print('It´s a tie!')

    
elif p2 == options[2]:
    if p1 == options[0]:
        print('Player1 WINS!')
    elif p1 == options[1]:
        print('Player2 WINS!')
    elif p1 == options[2] and p1 == options[2]:
        print('It´s a tie!')
        