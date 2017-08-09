#!/usr/bin/python3
'''
This example incorporates a number of the things we have learned so far this
semester and builds a game of rock, paper, scissors that a user can play
against the computer.
'''
import random

# Commonly, programmers will define module variables to be used as constants
# when they want to refer to specific strings repeatedly in their programs.
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def get_user_item():
    '''
    This function will ask the user for their item. The function will stay in
    the while loop until a valid answer is given.
    
    Returns:
        The validated user input
    '''
    item = input('What do you want, rock, paper, or scissors?: ')
    while item != ROCK and item != PAPER and item != SCISSORS:
        item = input('You have to pick rock, paper, or scissors '
                     '("{}" is invalid) Try again: '.format(item))
    return item
    

def get_computer_item():
    '''
    We'll use the random library to determine what item the computer gets.
    random.randint(0, 2) will return either 0, 1, or 2 and based on that, we
    can choose what item to return.
    
    Returns:
        One of rock, paper, or scissors
    '''
    r = random.randint(0, 2)
    if r == 0:
        return ROCK
    elif r == 1:
        return PAPER
    else:
        return SCISSORS
        
    
def determine_winner(player, computer):
    '''The rules of rock, paper, scissors are simple:
        rock beats scissors
        scissors beats paper
        paper beats rock
    If both sides have the same item, it's a draw
    
    Returns:
        'player' if the player's item wins
        'computer' if the computer's item wins
        'draw' if its a draw
    '''
    # When both sides have the same item, we can return immediately. This is
    # sometimes called a "short-circuit" path inside of a function because
    # we don't execute all of the function's body before returning.
    if player == computer:
        return 'draw'
    
    # Scenario 1: Player has rock, Computer must have paper or scissors
    winner = ''
    if player == ROCK:
        if computer == PAPER:
            winner = 'computer'
        else:
            winner = 'player'
        
    # Scenario 2: Player has paper, Computer must have scissors or rock
    if player == PAPER:
        if computer == SCISSORS:
            winner = 'computer'
        else:
            winner = 'player'
            
    # Scenario 3: Player has scissors, Computer must have rock or paper
    if player == SCISSORS:
        if computer == ROCK:
            winner = 'computer'
        else:
            winner = 'player'
    return winner
        

def main():
    '''
    Our main program should prompt the user to play their item until one side
    has won two games. It should then declare a winner.
    '''
    player_wins = 0
    computer_wins = 0
    game = 1
    
    # The loop's condition test will be True until one side has won two games
    while player_wins < 2 and computer_wins < 2:
        print('---------------------------------------------------------------')
        print('Game {}:'.format(game))
        # Get the item from the user (from input) and the computer (randomly)
        player = get_user_item()
        computer = get_computer_item()
        print('*** Player has {}, Computer has {} ***'.format(player, computer))
        
        # Call the determine_winner function to score the game.
        # Then, interpret the results.
        result = determine_winner(player, computer)
        if result == 'player':
            player_wins += 1
            print('Player wins!')
        elif result == 'computer':
            computer_wins += 1
            print('Computer wins!')
        else:  # Draw
            print('It\'s a draw. Keep playing')
        game += 1
    
    print('Thanks for playing')
        
main()
