class Tree():
    def __init__(self):
        return

    def add(self):
        return


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
