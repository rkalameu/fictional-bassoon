# Rock_Papper_Sissors
import random

print('---------------------------------')
print('Welcome to Rock, Paper, Scissors!')
print('---------------------------------')

print('1) is for (Rock)')
print('2) is for (Paper).')
print('3) is for (Scissors).')

player = int(input('player pick a number: '))
computer = random.randint(1,3)
#computer = 2

if player == computer:
 print(f'player: {player}')
 print(f'computer: {computer}') 
 print('Result: play again')
else:
 if player == 1 and computer == 2:
  print(f'player you choose {player} for Rock')
  print(f'computer choose{computer} for Papper')
  print('the computer won')
 elif player == 2 and computer == 1:
  print(f'player you choose {player} for Papper')
  print(f'computer choose {computer} for Rock')
  print('the player won') 
 elif player == 1 and computer == 3:
  print(f'player you choose {player} for Rock')
  print(f'computer choose {computer} for Sissors')
  print('the player won')  
 elif player == 3 and computer == 1:
  print(f'player you choose {player} for Sissors')
  print(f'computer choose {computer} for Rock')
  print('the computer won')  
 elif player == 2 and computer == 3:
  print(f'player you choose {player} for Papper')
  print(f'computer choose {computer} for Sissors')
  print('the computer won')  
 elif player == 3 and computer == 2:
  print(f'player you choose {player} for Sissors')
  print(f'computer choose {computer} for Papper')
  print('the player won')  
  
  # If you have any Tipps, please let me know

