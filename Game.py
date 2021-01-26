def main():
    while(True):
        board=list(map(int,'0'*9))
        print('Player 1 choose X or O')
        prompt=input('choise >> ')
        player1=0
        if prompt.lower()=='x':
            player1=1
            print('player 1 starts the game')
        elif prompt.lower()=='o':
            player1=2
            print('player 2 starts the game')
        else:
            continue
        display(board)
        game(board,player1)
        replay=input('if you want to replay enter Y/y else enter any key\n')
        if replay.lower()!='y':
            break
def win(board,player1):
    if board[0]==board[1]==board[2]!=0:
        return ['player 1' if board[0]==player1 else 'Player 2',True]
    if board[3]==board[4]==board[5]!=0:
        return ['player 1' if board[3]==player1 else 'Player 2',True]
    if board[6]==board[7]==board[8]!=0:
        return ['player 1' if board[6]==player1 else 'Player 2',True]
    if board[0]==board[3]==board[6]!=0:
        return ['player 1' if board[0]==player1 else 'Player 2',True]
    if board[0]==board[4]==board[8]!=0:
        return ['player 1' if board[0]==player1 else 'Player 2',True]
    if board[1]==board[4]==board[7]!=0:
        return ['player 1' if board[1]==player1 else 'Player 2',True]
    if board[2]==board[5]==board[8]!=0:
        return ['player 1' if board[2]==player1 else 'Player 2',True]
    if board[2]==board[4]==board[6]!=0:
        return ['player 1' if board[2]==player1 else 'Player 2',True]
    return ['Draw',False]
def game(board,player1):
    i=1
    while(True):
        print("\n\nplease choose your position")
        position=0;
        try:
            position=int(input("Position = "))
        except:
            continue
        if 1<=position<=9 and board[position-1]==0:
            board[position-1]=2 if i%2==0 else 1
        else:
            continue
        display(board)
        winner,winning=win(board,player1)
        if winning or i==9:
            break
        i+=1

    print('\n\nWinner  {} '.format(winner))
def display(board):
    count=0
    l=0
    print('\n')
    temp=board[6:9]+board[3:6]+board[0:3]
    for i in temp:
        if i==1:
            print(' X ' ,end='')
        elif i==2:
            print(' O ',end='')
        else:
            print('   ',end='')
        count+=1
        if count==3:
            count=0
            l+=1
            if l<=2:
                print('\n-----------')
        else:
            print('|',end='',sep='  ')
    print('\n')
main()
        
        
            
            
            
        
