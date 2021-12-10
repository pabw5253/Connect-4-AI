#
#This file contains the game. All the game's checks are in the check.py file
#Player vs. Ai uses col = check.takeInput(grid)
#AI vs. AI uses col = aix.check_ai(grid) and col = aio.check_ai(grid)
#
import pabwselConnect4Check as check
#####   X
import pabwselConnect4AI as aix
#import connect_4_LC_WZ as aix

#####   O
import pabwselConnect4AI as aio
#import connect_4_LC_WZ as aio


#create the grid. Grid is a list of strings
grid = []
for i in range(6):
    grid.append('-------')
    
#main code
if __name__=="__main__":
    #print the grid before game starts
    check.printGrid(grid)
    #choose who goes first
    turn = int(input("Who goes first? X(0) or O(1)? "))
    
    #take turns
    while True:
        a = ''
        if turn == 0:
            a = 'x'
            turn = 1
            #player aix
            col = aix.check_ai(grid, a)
            #col = check.takeInput(grid)
        elif turn == 1:
            a = 'o'
            turn = 0
            #player aio
            col = aio.check_ai(grid, a)
            #col = check.takeInput(grid)
        
        #turn move
        grid = check.playerTurn(grid, a, col)
        #print grid
        check.printGrid(grid)
        
        #find the top values for the later checks
        tops = check.findTops(grid)

        if sum(tops) == 0:
            break
     
        #check for a win
        #check columns
        xCol, oCol = check.column(grid, tops)
        #check rows
        xRow, oRow = check.row(grid, tops)
        #check diagonals
        xDiag, oDiag = check.diagonal(grid, tops)
        
        #check if someone wins the game
        winner = check.win(grid, tops)
        if check.win(grid, tops):
            if winner == 1:
                print("X wins!")
            if winner == 2:
                print("O wins!")
            
            break

if not winner:
    print("Cat's game!")