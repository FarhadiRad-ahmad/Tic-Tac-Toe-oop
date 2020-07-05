class Game:

    def __init__(self, position):
        if position != "":
            items = list(position)
            self.symbol = "X" if position.count("X") <= position.count("O") else "O"
        else:
            items = [" " for _ in range(9)]
            self.symbol = "X"

        self.field = [
            items[:3],
            items[3:6],
            items[6:],
        ]

    def check_win(self, symbol):
        pattern = [symbol, symbol, symbol]
        # for rows
        for row in self.field:
            if row == pattern:
                return True, f"{symbol} wins"
        # for columns
        for column in self.field_columns():
            if column == pattern:
                return True, f"{symbol} wins"
        # for columns
        for diagonal in self.field_diagonals():
            if diagonal == pattern:
                return True, f"{symbol} wins"
        return False, ""

    def field_columns(self):
        return [
            [self.field[0][0], self.field[1][0], self.field[2][0]],
            [self.field[0][1], self.field[1][1], self.field[2][1]],
            [self.field[0][2], self.field[1][2], self.field[2][2]]
        ]

    def field_diagonals(self):
        return [
            [self.field[0][0], self.field[1][1], self.field[2][2]],
            [self.field[2][0], self.field[1][1], self.field[0][2]]
        ]

    def count(self, symbol):
        result = 0
        for row in self.field:
            for item in row:
                if item == symbol:
                    result += 1
        return result

    def check_current_position(self):
        result, message = self.check_win(self.symbol)
        if result:
            return False, message
        elif self.count(" "):
            return True, None
        else:
            return False, "Draw"

    def draw_field(self):
        print("---------")
        for row in self.field:
            print("| ", end="")
            print(" ".join(row), end="")
            print(" |")
        print("---------")

    def convert_coordinates(self, x_im, y_im):
        x_real = abs(y_im - 3)
        y_real = x_im - 1
        return x_real, y_real

    def input_coordinates(self):
        while True:
            input_str = input("Enter the coordinates: ")
            if input_str.replace(" ", "").isdecimal():
                x_im, y_im = [int(i) for i in list(input_str.split())]
                if x_im in range(4) and y_im in range(4):
                    x, y = self.convert_coordinates(x_im, y_im)
                    break
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        return x, y

    def update_symbol(self):
        if self.symbol == "X":
            self.symbol = "O"
        else:
            self.symbol = "X"

    def move(self):
        x, y = self.input_coordinates()
        if self.field[x][y] == " ":
            self.field[x][y] = self.symbol
            game.draw_field()
        else:
            print("This cell is occupied! Choose another one!")
            self.move()


# initial_position = input("Enter cells: ")
game = Game("")
play = True
game.draw_field()
while play:
    game.move()
    play, message = game.check_current_position()
    game.update_symbol()
    if message is not None:
        print(message)
