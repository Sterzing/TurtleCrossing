from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self. goto(-280, 250)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)


# class Scoreboard():
#     def __init__(self):
#         self.next_level()
#
#     def next_level(self):
#         display_level = Turtle()
#         level = 0
#         display_level.penup()
#         display_level.hideturtle()
#         display_level.goto(-280, 250)
#         display_level.write(f"Level: {level}", False, "left", FONT)
#
#     def level_up(self):
#         display_level.clear()
#         level += 1
#         display_level.write(f"Level: {level}", False, "left", FONT)

    # def game_over_f(self):
    #     self.game_over.penup()
    #     self.game_over.hideturtle()
    #     self.game_over.goto(0, 0)
    #     self.game_over.write("GAME OVER", False, "center", FONT)