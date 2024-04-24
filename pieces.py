class Pieces:
    def __init__(self, color):
        self.color = color
        self.pieces = {
            "I1": [[color], [color], [color], [color], [color]],
            "I2": [[color], [color], [color], [color]],
            "I3": [[color], [color], [color]],
            "I4": [[color], [color]],
            "I5": [[color]],
            "O" : [[color, color], [color, color]],
            "O2": [[color, color], [color, color], [color, "."]],
            "T1": [[".", color, "."], [".", color, "."], [color, color, color]],
            "T2": [[".", color, "."], [color, color, color]],
            "L1": [[color, "."], [color, "."], [color, "."], [color, color]],
            "L2": [[color, "."], [color, "."], [color, color]],
            "L3": [[color, "."], [color, color]],
            "X" : [[".", color, "."], [color, color, color], [".", color, "."]],
            "V" : [[color, ".", "."], [color, ".", "."], [color, color, color]],
            "U" : [[color, ".", color], [color, color, color]],
            "W" : [[color, ".", "."], [color, color, "."], [".", color, color]],
            "Z" : [[color, "."], [color, color], [".", color], [".", color]],
            "Z2": [[color, "."], [color, color], [".", color]],
            "Z3": [[color, color, "."], [".", color, "."], [".", color, color]],
            "F1": [[color, "."], [color, color], [color, "."], [color, "."]],
            "F2": [[color, color, "."], [".", color, color], [".", color, "."]],
        }
        self.standardize_pieces() 
        self.piece_list = list(self.pieces.keys())

    def get_piece_shape(self, piece):
        return self.pieces[piece]

    def standardize_pieces(self):
        max_width = max(len(row) for piece in self.pieces.values() for row in piece)
        for piece_name, piece_shape in self.pieces.items():
            for i, row in enumerate(piece_shape):
                if len(row) < max_width:
                    # Extend the row with zeros to match the maximum width
                    self.pieces[piece_name][i] += ["."] * (max_width - len(row))
      