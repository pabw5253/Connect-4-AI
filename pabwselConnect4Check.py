
#import connect4ai as ai

grid = []

for i in range(6):
    grid.append('-------')


#prints the grid. Grid must be list of strings
def printGrid(grid):
    for i in range(6):
        #assert grid[i], ' | '.join(grid[i])
        a = ' | '.join(grid[i])
        print('|', a, '|')
    print('='*29)
    print()

#finds the index number of the row for each top of column
def findTops(grid):
    a = []
    for i in range(7):
        a.append(6)
        for j in range(6):
            if grid[j][i] != '-':
                a[i] = j
                break
    return a

#counts the number of Xs or Os in column
def column(grid, tops):
    a = []
    b = []
    for i in range(0, len(tops)):
        a.append(0)
        b.append(0)
        #makes sure that it does not go out of range of grid
        if tops[i] != 6:
            
            c = True
            for j in range(tops[i], 6):
                #if not the same as the value above, stop adding
                if grid[j][i] != grid[tops[i]][i]:
                    c = False
                if grid[j][i] == 'x':
                    if c:
                        a[i] += 1
                elif grid[j][i] == 'o':
                    if c:
                        b[i] += 1
    return a, b     # a is Xs, b is Os

#counts the number of Xs and Os in the row.
#sorted by column. Only checks rows near tops
def row(grid, tops):
    a = []
    b = []
    for i in range(len(tops)):
        a.append(0)
        b.append(0)
        if tops[i] != 6:
            c = grid[tops[i]]
            if i-3 >= 0:
                e = c[i-3:i+1].count('x')
                f = c[i-3:i+1].count('o')
                a[i] = e
                b[i] = f
            if i-2 >= 0 and i+1 < 7:
                e = c[i-2:i+2].count('x')
                f = c[i-2:i+2].count('o')
                a[i] = max(a[i], e)
                b[i] = max(b[i], f)
            if i - 1 >= 0 and i+2 < 7:
                e = c[i-1:i+3].count('x')
                f = c[i-1:i+3].count('o')
                a[i] = max(a[i], e)
                b[i] = max(b[i], f)
            if i+3 < 7:
                e = c[i:i+4].count('x')
                f = c[i:i+4].count('o')
                a[i] = max(a[i], e)
                b[i] = max(b[i], f)
    return a, b     #a is Xs, b is Os

#check the diagonals according to column
#only check columns near tops
def diagonal(grid, tops):
    a = []
    b = []
    for i in range(len(tops)):
        a.append(0)
        b.append(0)
        
        #down right
        c = ''
        if tops[i] != 6:
            c += grid[tops[i]][i]
            d = tops[i] + 1
            e = 1
            f = 0
            while d < 6 and i + e < 7 and f < 3:
                c += grid[d][i+e]
                d += 1
                e += 1
                f += 1
            g = c.count('x')
            h = c.count('o')
            a[i] = g
            b[i] = h
            
            #down left
            c = ''
            c += grid[tops[i]][i]
            d = tops[i] + 1
            e = 1
            f = 0
            while d < 6 and i - e > -1 and f < 3:
                c += grid[d][i-e]
                d += 1
                e += 1
                f += 1
            g = c.count('x')
            h = c.count('o')
            a[i] = max(a[i], g)     #cannot be greater than 4
            b[i] = max(b[i], h)     #cannot be greater than 4
            #print(c)
            
            #up right
            c = ''
            c += grid[tops[i]][i]
            d = tops[i] - 1
            e = 1
            f = 0
            while d > -1 and i + e < 7 and f < 3:
                c += grid[d][i+e]
                d -= 1
                e += 1
                f += 1
            g = c.count('x')
            h = c.count('o')
            a[i] = max(a[i], g)
            b[i] = max(b[i], h)
            
            #up left
            c = ''
            c += grid[tops[i]][i]
            d = tops[i] - 1
            e = 1
            f = 0
            while d > -1 and i - e > -1 and f < 3:
                c += grid[d][i-e]
                d -= 1
                e += 1
                f += 1
            g = c.count('x')
            h = c.count('o')
            a[i] = max(a[i], g)
            b[i] = max(b[i], h)
            
            #middle -2
            c = ''
            #c += grid[tops[i]][i]
            d = tops[i] - 2
            e = -2
            f = 0
            while 0 < d < 6 and -1 < i + e < 7 and f < 4:
                c += grid[d][i+e]
                d += 1
                e += 1
                f += 1
            g = c.count('x')
            h = c.count('o')
            a[i] = max(a[i], g)
            b[i] = max(b[i], h)
            
            #middle -1
            c = ''
            #c += grid[tops[i]][i]
            d = tops[i] - 2
            e = -1
            f = 0
            while 0 < d < 6 and -1 < i + e < 7 and f < 4:
                c += grid[d][i+e]
                d += 1
                e += 1
                f += 1
            g = c.count('x')
            h = c.count('o')
            a[i] = max(a[i], g)
            b[i] = max(b[i], h)
    return a, b

#checks for a win at the tops
def win(grid, tops):
    a, b = column(grid, tops)
    c, d = row(grid, tops)
    e, f = diagonal(grid, tops)
    #if (4 in a) or (4 in b) or (4 in c) or (4 in d) or (4 in e) or (4 in f):
     #   return True
    if 4 in a or 4 in c or 4 in e:
        return 1
    if 4 in b or 4 in d or 4 in f:
        return 2
    if sum(tops) == 0:
        return -1
    return 0

#takes player input
def takeInput(grid):
    col = input("=> ")
    if col.isdigit() == False:
        col = takeInput(grid)
        return col
    col = int(col)
    if col > 6 or col < 0:
        col = takeInput(grid)
        return col
    if grid[0][int(col)] != '-':
        col = takeInput(grid)
        return col
    return col

#places piece in column
def playerTurn(grid, turn, col):
    for i in range(6):
        if grid[5-i][col] == '-':
            grid[5-i] = ' '.join(grid[5-i])
            grid[5-i] = grid[5-i].split()
            grid[5-i][col] = turn
            grid[5-i] = ''.join(grid[5-i])
            return grid
    return grid

