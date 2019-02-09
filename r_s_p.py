# ROCK PAPER SCISSORS
# BASIC VERSION V 1.0
# DEC. 14. 2018

print('#' * 50)
print()
print('START GAME ' * 4)
print()
print('#' * 50)

soup = ['rock', 'paper', 'scissors']

while True:
    p1 = input('Enter player 1´s choice: ')
    print('#NO CHEATING#')
    
    no_cheating = ('#NO CHEATING#')
    #repete 'no cheating'
    for i in range(50):
        print(no_cheating)
        
    p2 = input('Enter player 2´s choice: ')

    if p1 and p2 in soup:
        print('SHOOT!')
        break
    else:
        print('Try again! (not found)')

if p1 == soup[0] and p2 == soup[1]:
    print('Player2 WINS!')

elif p1 == soup[0] and p2 == soup[2]:
    print('Player1 WINS!')

elif p1 == soup[0] and p2 == soup[0]:
    print('It´s a TIE!')
    
#####################################
elif p1 == soup[1] and p2 == soup[0]:
    print('Player1 WINS!')

elif p1 == soup[1] and p2 == soup[2]:
    print('Player2 WINS!')

elif p1 == soup[1] and p2 == soup[1]:
    print('That´s a TIE!')
#####################################

elif p1 == soup[2] and p2 == soup[0]:
    print('Player2 WINS!')

elif p1 == soup[2] and p2 == soup[1]:
    print('Player1 WINS!')

elif p1 == soup[2] and p2 == soup[2]:
    print('It´s a TIE!')
#####################################

####
#p2#
####

elif p2 == soup[0] and p1 == soup[1]:
    print('Player2 WINS!')

elif p2 == soup[0] and p1 == soup[2]:
    print('Player2 WINS!')

elif p2 == soup[0] and p1 == soup[0]:
    print('It´s a TIE!')
    
#######################################

elif p2 == soup[1] and p1 == soup[0]:
    print('Player1 WINS!')
    
elif p2 == soup[1] and p1 == soup[2]:
    print('Player2 WINS!')

elif p2 == soup[1] and p1 == soup[1]:
    print('It´s a TIE!')
    
######################################

elif p2 == soup[2] and p1 == soup[0]:
    print('Player2 WINS!')

elif p2 == soup[2] and p1 == soup[1]:
    print('Player1 WINS!')
    
elif p2 == soup[2] and p1 == soup[2]:
    print('It´s a TIE!')










