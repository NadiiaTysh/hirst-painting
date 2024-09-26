from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

from PIL.ImageChops import screen

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

color_list = [(228, 224, 211), (225, 159, 74), (38, 104, 150), (122, 166, 191), (158, 60, 83), (194, 160, 28),
              (199, 135, 157), (216, 85, 58), (168, 79, 49), (24, 135, 102), (204, 83, 110), (213, 228, 216),
              (122, 183, 153), (148, 29, 37), (235, 198, 103), (51, 167, 133), (232, 208, 218), (38, 162, 185),
              (3, 111, 94), (202, 220, 228), (28, 62, 115), (119, 112, 160), (235, 164, 181), (129, 34, 31),
              (25, 57, 85), (239, 162, 155), (160, 211, 200), (58, 43, 42), (62, 40, 56), (145, 208, 216)]

timmy = Turtle()

# Set position left bottom corner
x = -225
y = -225
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setpos(x, y)

# Move up 10 times
for row in range(10):
    # Draw 10 dots
    for col in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

    timmy.setpos(x, (row + 1) * 50 + y)

# timmy.setheading(225)
# timmy.forward(300)
# timmy.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     timmy.dot(20, random.choice(color_list))
#     timmy.forward(50)
#
#     if dot_count % 10 == 0:
#         timmy.setheading(90)
#         timmy.forward(50)
#         timmy.setheading(180)
#         timmy.forward(500)
#         timmy.setheading(0)


view_screen = Screen()
view_screen.exitonclick()
