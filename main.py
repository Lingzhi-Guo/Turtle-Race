import random
import turtle
from turtle import Turtle, Screen

game_on = False
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtles = []
x = -450
y = -150

for num in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[num])
    timmy.goto(x, y)
    y += 50
    turtles.append(timmy)

if user_bet:
    game_on = True


while game_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
    if turtle.xcor() > 300:
        winning_color = turtle.pencolor()
        game_on = False
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You lost. The {winning_color} turtle is the winner.")

screen.exitonclick()
