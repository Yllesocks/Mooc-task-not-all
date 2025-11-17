def chessboard(x):
    index = 0
    while index < x:
        chess = "1010101010101010" * x
        print(chess[index: index + x])
        index += 1

if __name__ == "__main__":
    chessboard(4)
       

if __name__ == "__main__":
    chessboard(3)