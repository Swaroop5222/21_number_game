import random

def find21(game_list):
    for i in game_list:
        if i==21:
            return True
    return False

def computer(game_list):
    print('Computer turn')
    print('Numbers present in the list are: ',game_list)
    if not find21(game_list):
        choose=random.randint(1,min(3,22-len(game_list)))
    for i in range(choose):
        last_num=game_list[-1]
        if last_num<22:
            game_list.append(last_num+1)

def player(game_list):
    print('Your turn')
    print('Numbers present in the list are: ',game_list)
    while(True):
        count=int(input("Enter count of numbers you want to enter in the list(only 1-3): "))
        if count<0 or count>3:
            print("Enter number between 1 to 3 only")
            continue
        elif count>=0 and count<=3:
            if count<=(22-len(game_list)):
                for i in range(count):
                    last_num=game_list[-1]
                    if last_num<22:
                        game_list.append(last_num+1)
                break
        else:
            print('Enter proper count')

def game_winner(winner):
    if winner=='player':
        print('Final list is: ',game_list)
        print('Congratulations you have beat the conputer and won the game')
    elif winner=='computer':
        print('Final list is: ',game_list)
        print('Oops! you have lost')
        print('Better luck next time')
    else:
        pass
    
def start():
    choice=input("Enter \'f\' to start first or enter \' s\' to start second: ").lower()
    winner=None
    if choice=='f':
        while(not find21(game_list)):
            player(game_list)
            if find21(game_list):
                winner='computer'
                break
            computer(game_list)
            if find21(game_list):
                winner='player'
                break
        game_winner(winner)
    elif choice=='s':
        while(not find21(game_list)):
            computer(game_list)
            if find21(game_list):
                winner='player'
                break
            player(game_list)
            if find21(game_list):
                winner='computer'
                break
        game_winner(winner)
    else:
        print('Enter valid choice.')
        
winner=''
while(True):
    game_list=[0]
    ask=input("Do you want to play the game?(y/n) only: ")
    if ask=='y':
        start()
    elif ask=='n':
        print('Game ended')
        print('Hope you enjoyed the game')
        break
    else:
        print('Enter either y or n only')