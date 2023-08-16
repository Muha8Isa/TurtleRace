from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)

while True:
    colour = ["red", "orange", "yellow", "green", "blue", "purple"]
    user_bet = screen.textinput(title="Make your bet!", prompt=f"Which turtle will win the race?\n{colour} \nEnter a colour: ").lower()
    if user_bet in colour:
        break


turtles = []

name = ""
for i, j in enumerate(colour):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(j)
    new_turtle.penup()
    new_turtle.goto(x=-230, y= -120 + i*50)
    turtles.append(new_turtle)

result = Turtle()
result.penup()
result.goto(0,0)
result.hideturtle()


on = True
win = False
while on:
    for i in turtles:
        i.fd(random.uniform(0.1, 1) * 10)
        if i.xcor() >= 230:
            on = False
            if user_bet == i.pencolor():
                win = True
                result.write(f"Congrats the {user_bet} won the race")
            else:
                result.write(f"You lost, {i.pencolor()} won the race")
                break


# if win:
#     result.write(f"Congrats the {user_bet} won the race")
# else:
#     result.write(f"You lost, {i.pencolor()} won the race")

screen.exitonclick()