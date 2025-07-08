from PIL import Image
import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

class CrossingGame:
    def __init__(self,
                 level: int = 1,
                 screen_size: int = 600,
                 controls: dict[str, str] = None
                 ):
        self.running = True
        if controls is None:
            self.controls = {
                "w": "Up",
                "Up": "Up",
                "a": "Left",
                "Left": "Left",
                "d": "Right",
                "Right": "Right",
                "s": "Down",
                "Down": "Down",
            }
        else:
            self.controls = controls
        self.level = level
        self.screen_width = screen_size
        self.screen_height = screen_size
        self.screen = Screen()
        self.screen.setup(width = self.screen_width, height = self.screen_height)

        """
        Resizing the image to fit the screen
        """
        original_image_path = "scene_1.gif"
        resized_image_path = "scene_1_resized.gif"

        try:
            img = Image.open(original_image_path)
            resized_img = img.resize((self.screen_width, self.screen_height),
                                     Image.Resampling.LANCZOS)
            resized_img.save(resized_image_path, format="GIF")

            print(f"Image created correctly {resized_image_path}")

        except FileNotFoundError:
            print(f"Error: Field not found {original_image_path}")
        except Exception as e:
            print(f"An error happen: {e}")

        """
        End of resizing the image
        """

        self.screen.bgpic("scene_1_resized.gif")
        self.screen.title("Turtle Crossing Game")
        self.screen.getcanvas().winfo_toplevel().resizable(False, False)

        self.screen.tracer(0)

        # Create the start spot and the goal one
        self.goal = self.screen_width / 2 - self.screen_width * 0.065
        self.start = -self.screen_width / 2 + self.screen_width * 0.065
        self.start_position: tuple[float, float] = (-self.screen_width / 2 + 185, self.start)

        self.scoreboard = Scoreboard(level = self.level, screen_width = self.screen_width, screen_height = self.screen_height)
        self.car = Car(screen_width = self.screen_width, screen_height = self.screen_height)
        self.player = Player(start_position = self.start_position, screen_width = self.screen_width, screen_height = self.screen_height)

        self.screen.listen()
        for key_char, action_name in self.controls.items():
            self.screen.onkeypress(key=key_char, fun=lambda action=action_name: self.move_player(action))

        self.start_game()
        self.screen.exitonclick()

    def reposition_player(self):
        self.player.goto(self.start_position)

    def up_level(self):
        self.level += 1
        self.scoreboard.level = self.level
        self.car.level = self.level
        self.player.level = self.level
        self.scoreboard.update_scoreboard()
        self.reposition_player()

    def move_player(self, action: str):
        if action == "Up":
            if self.player.ycor() < self.goal:
                self.player.go_up()
            else:
                if self.level == 5:
                    self.up_level()
                    print("You win!")
                    self.running = False
                else:
                    self.up_level()
        if action == "Left" and self.level < 4:
            self.player.go_left()
        if action == "Right" and self.level < 4:
            self.player.go_right()
        if action == "Down" and self.level < 3 and self.player.ycor() > self.start:
            self.player.go_down()

    def move_cars(self):
        for car in self.car.list_of_cars:
            car.forward(20)

    def check_collision(self):
        for car in self.car.list_of_cars:
            if car.distance(self.player) < 30:
                self.running = False
                self.scoreboard.lose()
                print("You lose!")
                break

    def start_game(self):
        while self.running:
            self.screen.update()
            time.sleep(0.1)
            self.car.create_car()
            self.move_cars()
            self.car.destroy_car()
            self.check_collision()


