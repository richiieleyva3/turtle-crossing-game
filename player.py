from turtle import Turtle

class Player(Turtle):
    def __init__(self,
                 start_position: tuple[float, float] = (0, -280),
                 screen_width: int = 600,
                 screen_height: int = 600,
                 ):
        super().__init__()
        self.level = 1
        self.start_position = start_position
        self.screen_width = screen_width
        self.screen_height = screen_height
        register_ok = self.register_turtle()
        if not register_ok:
            self.shape("turtle")
        else:
            self.shape("turtle.gif")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.goto(self.start_position)

    def register_turtle(self):
        try:
            if not hasattr(self, 'screen'):
                raise AttributeError("Screen not initialized")

            self.screen.register_shape(f"turtle.gif")
            return True
            #print(f"Car {i} created successfully.")

        except FileNotFoundError:
            print(f"Error: turtle.gif file not found")
            return False
        except AttributeError as e:
            print(f"Error: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def go_up(self):
        if self.level < 5:
            self.forward(15)
        else:
            self.forward(8)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_down(self):
        self.backward(15)