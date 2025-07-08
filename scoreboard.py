from turtle import Turtle
FONT = ("Courier", 16, "bold")
FONT_2 = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self, level: int = 1, screen_width: int = 600, screen_height: int = 600):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level = level
        self.hideturtle()
        self.penup()
        self.goto(-self.screen_width / 2 + self.screen_width * 0.95, self.screen_height / 2 - 50)
        self.color("white")
        self.write(f"Level: {self.level}", align="right", font=FONT)
        self.level_instructions = Turtle()
        self.level_instructions.hideturtle()
        self.level_instructions.penup()
        self.level_instructions.goto(-self.screen_width / 2 + self.screen_width * 0.95, self.screen_height / 2 - 30)
        self.level_instructions.color("white")
        self.level_instructions.write(f"Free move and normal speed", align="right", font=FONT_2)
        #self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level_instructions.clear()
        if self.level == 1:
            self.write(f"Level: {self.level}", align="right", font=FONT)
            self.level_instructions.write(f"Free move and normal speed", align="right", font=FONT_2)
        elif self.level == 2:
            self.write(f"Level: {self.level}", align="right", font=FONT)
            self.level_instructions.write(f"Free move and fast speed", align="right", font=FONT_2)
        elif self.level == 3:
            self.write(f"Level: {self.level}", align="right", font=FONT)
            self.level_instructions.write(f"You can't backward", align="right", font=FONT_2)
        elif self.level == 4:
            self.write(f"Level: {self.level}", align="right", font=FONT)
            self.level_instructions.write(f"You only can forward", align="right", font=FONT_2)
        elif self.level == 5:
            self.write(f"Level: {self.level}", align="right", font=FONT)
            self.level_instructions.write(f"You only can forward more slow", align="right", font=FONT_2)
        else:
            self.write(f"You win!", align="right", font=FONT)

    def lose(self):
        self.clear()
        self.level_instructions.clear()
        self.write(f"You lose!", align="right", font=FONT)

