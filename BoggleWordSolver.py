class Tree():
    def __init__(self, letter = None):
        self.letter = letter
        self.children = {}
        self.leaf = False

    # add a word, letter by letter    
    def add(self, word):
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = Tree(letter)
            return self.children[letter].add(word)    
        else:
            leaf = True
            return self   

    

    # locate a letter in the tree
    def search(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]    

#function for the actual word solver

def findWord(board, tree, validated, row, col, path=None, currLetter = None, word = None):
    letter = board[row][col]
    if path is None or currLetter is None or word is None:
        currLetter = tree.search(letter)
        path = [(row, col)]
        word = letter
    else:
        currLetter = currLetter.search(letter)
        path.append((row, col))
        word = word + letter

    # Base cases 
    if currLetter is None:
        return
    if currLetter.leaf:
        validated.add(word)


def main():
   # print("Hello")

    # initialize the game board
    board = []
    for i in range(0,4):
        # append empty row
        board.append([])
        for j in range(0,4):
            board[i].append(input().strip().upper())

    # print board
    for i in range(0,4):
        for j in range(0,4):
            print(board[i][j], end = " ")
        print()    


    # load dictionary
    dict = open('dictionary-yawl.txt', "r")

    tree = Tree()

    for line in dict:
        word = line.rstrip().upper()
        tree.add(word)

main()
