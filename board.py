from pieces import Pieces

class board: 
    def __init__(self, size):
        # create blockus duo board
        self.size = max(14, size)
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.white = "W"
        self.black = "B"
        self.white_pieces = Pieces(self.white)
        self.black_pieces = Pieces(self.white)

    def print_board(self):
        for row in self.board:
            print(row)

    def print_pieces(self):
        for piece_name, piece_shape in self.white_pieces.pieces.items():
            print(piece_name + ":")
            for row in piece_shape:
                print(' '.join(map(str, row)))  # Join the elements of each row with a space
            print()  # Print an empty line after each piece
        for piece_name, piece_shape in self.black_pieces.pieces.items():
            print(piece_name + ":")
            for row in piece_shape:
                print(' '.join(map(str, row)))  # Join the elements of each row with a space
            print()  # Print an empty line after each piece

    def get_piece(self, piece, color):
        if color == self.white:
            return self.white_pieces.get_piece_shape(piece)
        else:
            return self.black_pieces.get_piece_shape(piece)


def main():
    b = board(8)
    b.print_board()
    print(b.size)
    b.print_pieces()   


if __name__ == "__main__":
    main()