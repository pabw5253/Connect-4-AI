import pabwselConnect4Check as check


#function with ai
def check_ai(grid, turn):
    w = ''
    if turn == 'x':
        w = 'o'
    if turn == 'o':
        w = 'x'
    #copy grid
    g = grid.copy()
    h = []
    j = []
    #
    #This part of the code adds a piece at i, checks for a win
    #checks each position, and removes the piece at i
    #
    for i in range(7):
        h.append(0)
        j.append(0)
        #places a move
        g = check.playerTurn(g, turn, i)
        
        #finds index of tops
        tops = check.findTops(g)
        
        #checks if there is a win
        winner = check.win(g, tops)
        if winner:
            return i
        
        #checks the colums, rows, and diagonals
        if turn == 'o':
            a, b = check.column(g, tops)
            c, d = check.row(g, tops)
            e, f = check.diagonal(g, tops)
        elif turn == 'x':
            b, a = check.column(g, tops)
            d, c = check.row(g, tops)
            f, e = check.diagonal(g, tops)
        
        #take the min of sums
        #h[i] = max(sum(a), sum(c), sum(e))
        j[i] = max(max(b), max(d), max(f))
        
        #checks the Xs for future possible opponent moves
        for k in range(7):
            if tops[k] != 0:
                g = check.playerTurn(g, w, k)
                tops = check.findTops(g)
                
                if turn == 'o':
                    a, b = check.column(g, tops)
                    c, d = check.row(g, tops)
                    e, f = check.diagonal(g, tops)
                elif turn == 'x':
                    b, a = check.column(g, tops)
                    d, c = check.row(g, tops)
                    f, e = check.diagonal(g, tops)
                
                """winner = check.win(g, tops)
                if winner:
                    print(winner)
                    h[i] = 100"""
                    
                h[i] = max(h[i], sum(a), sum(c), sum(e))
                #j[i] = max(j[i], max(b), max(d), max(f))
                
                r = ''
                for q in range(len(g[tops[k]])):
                    if q != k:
                        r += g[tops[k]][q]
                    else:
                        r += '-'
                g[tops[k]] = r
                
                   
        """r = ''
        tops = check.findTops(g)
        for q in range(len(g[tops[i]])):
            if q != i and g != grid:
                r += g[tops[i]][q]
            else:
                r += '-'
        g[tops[i]] = r
        #g[tops[i]][i] = '-'"""
        g = grid.copy()
        
    tops = check.findTops(g)
    #print(tops)
    for i in range(len(tops)):
        if tops[i] == 0:
            #print('a', tops)
            h[i] = 100
            j[i] = 100
            
    a = max(min(h), min(j))
    #a = min(h)
    #a = min(max(k), max(j))
    #print(h, j)
    if a in h:
        s = h[::-1]
        t = s.index(min(s))
        return 6-t #h.index(max(h))
    if a in j:
        return j.index(min(j))