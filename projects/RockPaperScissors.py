#take in a number 0-2 from the user that represents their hand
#generate a random number 0-2 to use for the computer's hand
#call the function get_hand to get the string representation of the user's hand
#call the function get_hand to get the string representation of the computer's hand
#call the function determine_winner to figure out who won
#print out the player hand and computer hand
#print out the winner
import random
player = int(input("Enter your hand (0=S, 1=R, 2=P): "))
PC = random.randint(0,2)

def get_hand(hand):
    #print(hand)
    stringhand = ""
    if hand == 0:
        stringhand = stringhand + "Paper"
    if hand == 1:
        stringhand = stringhand + "Scissors"
    if hand == 2:
        stringhand = stringhand + "Rock"
    return stringhand
    
print(f'Your selection: {get_hand(player)}')
print(f'PC selection: {get_hand(PC)}')
playerhand = get_hand(player)
PChand = get_hand(PC)
#print(playerhand)
#print(PChand)

def determine_winner(playerresult, PCresult):
    winner = ""
    if playerresult == "Rock" and PCresult == "Scissors":
        winner = winner + "You!"
          
    if playerresult == "Paper" and PCresult == "Scissors":
        winner = winner + "The PC!"
          
    if playerresult == "Rock" and PCresult == "Paper":
        winner = winner + "None of you!"
          
    if playerresult == PCresult:
        winner = winner + "None of you!"
       
    return winner
    
print(f'The winner is: {determine_winner(playerhand, PChand)}')