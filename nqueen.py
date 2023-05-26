#n-queen is a problem of placing n queens on a n*n chess board such that no queen can attack any other queens on the board. 
#The queen can attack horizontally, vertically and diagonally.
#This is a recursive solution to the n-queen problem.
#The solution is based on the backtracking algorithm.


N = int(input("Enter the number of queens: "))

board = [[0]*N for _ in range(N)] #create a 2d array of size N*N and initialize it with 0

def isAttack(i,j):  #function to check if a queen can attack another queen
    for k in range(N):  #for every row and column
        if (board[i][k] == 1 or board[k][j] == 1):
            return True
        
    for k in range(N):    #for every diagonal
        for m in range(N):
            if ((k+m == i+j) or (k-m == i-j)):
                if board[k][m] == 1:
                    return True
    return False

def NQueen(n):   #function to place n queens on the board
    if n==0:
        return True
    
    for i in range(N):  #for every row and column
        for j in range(N):
            if not(isAttack(i,j)) and (board[i][j]!=1):
                board[i][j] = 1
                
                if NQueen(n-1)==True: #recursive call
                    return True
                
                board[i][j] = 0   #backtracking
    return False


#Driver Code
NQueen(N)

#print the board
for i in board:
    print(i)