from turtle import Turtle, Screen
from svgpathtools import parse_path
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self,
                 screen_width: int = 600,
                 screen_height: int = 600,
                 ):
        super().__init__()
        self.level = 1
        self.amount_of_cars = 8
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = Screen()
        self.hideturtle()
        self.cars_spots = {
            "car_line_1": -self.screen_width / 2 + self.screen_width * 0.141,
            "car_line_2": -self.screen_width / 2 + self.screen_width * 0.225,
            "car_line_3": -self.screen_width / 2 + self.screen_width * 0.308,
            "car_line_4": -self.screen_width / 2 + self.screen_width * 0.391,
            "car_line_5": -self.screen_width / 2 + self.screen_width * 0.475,
            "car_line_6": self.screen_width / 2 - self.screen_width * 0.450,
            "car_line_7": self.screen_width / 2 - self.screen_width * 0.375,
            "car_line_8": self.screen_width / 2 - self.screen_width * 0.291,
            "car_line_9": self.screen_width / 2 - self.screen_width * 0.216,
            "car_line_10": self.screen_width / 2 - self.screen_width * 0.133,
        }
        self.screen.register_shape("car", self.create_shape_with_svg())
        self.register_all_the_gif_shapes()
        self.list_of_cars = []

    def register_car(self, i: int):
        try:
            if not hasattr(self, 'screen'):
                raise AttributeError("Screen not initialized")

            self.screen.register_shape(f"car_{i}.gif")
            #print(f"Car {i} created successfully.")

        except FileNotFoundError:
            print(f"Error: car_{i}.gif file not found")
            self.create_shape_with_svg()
        except AttributeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def create_car(self):
        # Lucky determined the speed creation of the cars
        # Normal speed
        if self.level == 1:
            if random.randint(1, 6) != 2:
                return
        # Fast speed
        else:
            if random.randint(1, 3) != 2:
                return


        new_car = Turtle()
        new_car.penup()
        i = random.randint(1, self.amount_of_cars)
        new_car.shape(f"car_{i}.gif")
        #new_car.shapesize(stretch_wid=0.35, stretch_len=0.35)
        new_car.shapesize(stretch_wid=0.035, stretch_len=0.035)
        new_car.color(random.choice(COLORS))
        new_car.goto(-self.screen_width / 2 - 50, self.cars_spots[f"car_line_{random.randint(1, 10)}"])
        self.list_of_cars.append(new_car)

    def register_all_the_gif_shapes(self):
        for i in range(1, self.amount_of_cars + 1):
            self.register_car(i)

    def destroy_car(self):
        """
        Destroy the car when it is out of the screen
        """
        for car in self.list_of_cars:
            if car.xcor() > self.screen_width / 2 + 50:
                self.list_of_cars.remove(car)
                car.hideturtle()
                car.clear()
                car.penup()
                break

    @staticmethod
    def create_shape_with_svg():
        d = "M4348.55 13481.14c184.07,-106.52 863.86,-243.57 874.77,-1060.61 10.59,-792.87 -661.93,-969.13 -832.16,-1113.11 -30.78,-1129.04 22.78,-2330.42 20.07,-3472.65l-41.53 -3499.15c223.3,-155.08 302.45,-139.01 536.53,-425.15 164.48,-201.06 198.11,-512.17 160.42,-820.23 -62.59,-511.67 -314.41,-774.58 -729.52,-940.05 -119.51,-47.64 -90.83,-11.38 -102.21,-155.7 -41.7,-529.19 -54.35,-1271.94 -187.04,-1757.83 -45.7,-167.34 -60.1,-202.25 -253.37,-229.69 -355.88,-50.53 -830.34,184.82 -1094.07,371.67 -214.8,152.19 -324.97,-11.26 -842.47,-1.11 -364.05,7.13 -549.93,60.91 -508.54,437.97 65.34,595.29 -36.21,1139.27 -206.06,1664.3 -248.9,769.39 -910.63,1406.31 -1078.23,2813.98 -147.93,1242.4 -38.65,2328.1 275.18,3476.69 153.17,560.6 364.06,839.22 670.94,1263.85 833.52,1153.37 883.08,1212.12 1167.78,2700.98 142.82,746.92 213.83,1734 857.71,2033.44 178.41,82.97 594.47,182.84 810.51,174.64 702.82,-26.68 397.66,-563.05 501.29,-1462.22z"

        path = parse_path(d)
        n = 100
        pts = [path.point(i / (n - 1)) for i in range(n)]

        xs = [p.real for p in pts]
        ys = [p.imag for p in pts]
        cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
        scale = max(max(xs) - min(xs), max(ys) - min(ys)) / 200

        cords = [((p.real - cx) / scale, (p.imag - cy) / scale) for p in pts]

        return tuple((round(x, 2), round(y, 2)) for x, y in cords)
