import random
#fork
wins = 0
loses = 0

while wins < 3 and loses < 3:
    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_turn = 'Rock'
    elif computer_choice == 2:
        computer_turn = 'Paper'
    elif computer_choice == 3:
        computer_turn = 'Scissors'

    print('Enter 1 for rock, 2 for paper, 3 for scissors,')
    user_choice = int(input('Your turn: '))

    if user_choice == 1:
        user_turn = 'Rock'
    elif user_choice == 2:
        user_turn = 'Paper'
    elif user_choice == 3:
        user_turn = 'Scissors'

    print(f"{user_turn} vs. {computer_turn}")

    user_wins = user_turn == 'Rock' and computer_turn == 'Scissors' or\
                user_turn == 'Scissors' and computer_turn == 'Paper' or\
                user_turn == 'Paper' and computer_turn == 'Rock'

    if user_wins:
        print("User wins this round")
        wins += 1
    elif user_turn == computer_turn:
        print("Draw")
    else:
        print("Computer wins this round")
        loses += 1

    print(f"{wins}:{loses}")

    if wins == 3:
        print('Player wins!')
        break
    if loses == 3:
        print('Computer wins!')
        break
