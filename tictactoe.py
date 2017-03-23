import sys
globalState = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
globalMove  = [['1','2','3'],['4','5','6'],['7','8','9']]
globalSetMove = set('123456789')

def drawLine(lineState):
    print "| %s | %s | %s |" % (lineState[0],lineState[1], lineState[2])

def drawBoard(gameState):
    print "-------------"
    drawLine(gameState[0])
    print "-------------"
    drawLine(gameState[1])
    print "-------------"
    drawLine(gameState[2])
    print "-------------"

def drawMove():
    drawBoard(globalMove)

def moveToIndex(inputMove):
    '''
    temp = int(inputMove)-1
    print "inputMove as int: %s" % temp
    return temp
    '''
    return int(inputMove)-1

def moveCheck(inputMove):
    if( inputMove not in globalSetMove ):
        print "Not a move, enter 123456789"
        return false
    temp = moveToIndex(inputMove)
    if(globalState[temp / 3][temp % 3] != ' '):
        print "spot already taken! Invalid move."
        return False
    return True

def winCheck():

    # check middle: middle col, middle row, both diags
    if(globalState[1][1] != ' ' and ( \
        globalState[0][1] == globalState[1][1] == globalState[2][1] or \
        globalState[1][0] == globalState[1][1] == globalState[1][2] or \
        globalState[0][0] == globalState[1][1] == globalState[2][2] or \
        globalState[0][2] == globalState[1][1] == globalState[2][0] \
        )):
        return True

    # then upper left:down col and cross col
    if(globalState[0][0] != ' ' and ( \
        globalState[0][0] == globalState[1][0] == globalState[2][0] or \
        globalState[0][0] == globalState[0][1] == globalState[0][2] \
        )):
        return True
    # then upper right:down col
    if(globalState[0][2] != ' ' and ( \
        globalState[0][2] == globalState[1][2] == globalState[2][2] \
        )):
        return True
    #lowest row
    return globalState[2][0] != ' ' and \
        globalState[2][0] == globalState[2][1] == globalState[2][2]

def updateState(move, xOrO):
    if(xOrO == 'X' or xOrO == 'O'):
        temp = moveToIndex(move)
        globalState[temp / 3][temp % 3] = xOrO
        return
    else:
        print "something is wrong, not X or O"
    return

def playTic():
    print "the current state of the game: \n\n"
    drawBoard(globalState)
    print "X goes first"
    turn = 'X'
    for i in xrange(9):
        print "state of board:"
        drawBoard(globalState)
        print "Where would you like to move, %s?\n \
Enter the number corresponding to the position.\n" % turn
        drawMove()
        for x in xrange(5):
            inputMove = raw_input("Enter your move: ")
            if(not moveCheck(inputMove)):
                print "invalid move entered, try again."
                continue
            else:
                break
        else:
            print "Too many invalid move attempts, exiting"
            return
        updateState(inputMove, turn)
        if(i>2 and winCheck()):
            print "%s wins!" % turn
            break
        if(turn == 'X'):
            turn = 'O'
        else:
            turn = 'X'
    print "end game, game state:"
    drawBoard(globalState)
    return
