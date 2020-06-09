X = "X"
O = "O"
EMPTY = None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def findwinner(board, p):
        for row in board:
            if all(tile==p for tile in row):
                return p
        for i in range(3):
            if all([row[i]==p for row in board]):
                return p 
        if all([board[i][i]==p for i in range(3)]):
            return p
        if all([board[::-1][i][i]==p for i in range(3)]):
            return p
    if findwinner(board, "O") == "O": return "O"
    elif findwinner(board, "X") == "X": return "X"
    return None 

board = [[X, X, X],
            [X, X, X],
            [X, X, X]]

# # print(any([True for row in board if EMPTY in row]))
# a = set([1,3,4])
# b = set([2,3,4,5])
# print([num for num in a if num not in b])

# cell = (3,3)
# neighbors = [(i - 1 + cell[0], j - 1 + cell[1]) for 
#             i in range(3) for j in range(3) 
#             if (i - 1 + cell[0]) >= 0
#              and (j - 1 + cell[1]) >= 0 
#              and (i - 1 + cell[0], j - 1 + cell[1]) != cell]
# print(neighbors)

a = set([1,3,4])
b = set([1,3])
k = [a, b]

for s in k: 
    for j in k: 
        if s.issubset(j):
            print(s)
            break

# for sentence in self.knowledge: #5)
#     for sen in self.knowledge: 
#         if sentence.cells.issubset(sen.cells):
#             tempsen = Sentence(sentence.cells - sen.cells, sentence.count - sen.count)
#             if tempsen not in self.knowledge:
#                 self.knowledge.append(tempsen)
