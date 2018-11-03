import random


def input_human_play(input=input):
    play = input('rock, paper, scissors?')
    while not is_valid_play(play):
        play = input('rock, paper, scissors?')
    return play


def is_valid_play(play):
    #return True
    return play in ['rock', 'paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate_game(human, computer):
    if human == computer:
        return 'tie'
    elif (human == 'rock' and computer == 'paper') or (human == 'paper' and computer == 'scissors') or (human == 'scissors' and computer == 'rock'):
        return 'computer'
    elif (computer == 'rock' and human == 'paper') or (computer == 'paper' and human == 'scissors') or (computer == 'scissors' and human == 'rock'):
        return 'human'

def main(input=input): #dependency injection
    human = input_human_play(input)
    computer = generate_computer_play()

    print(computer)

    game = evaluate_game(human, computer)
    if game == 'tie':
        print('it is a tie')
    else:
        print (f'{game}won')

if __name__ == '__main__':
    main()
