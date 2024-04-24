from board import board

def main(): 
    b = board(14)
    white_pieces = b.get_pieces(b.white)
    black_pieces = b.get_pieces(b.black)
    print(white_pieces)
    print(black_pieces)
    b.print_piece("I1", b.white)


if __name__ == "__main__":
    main()