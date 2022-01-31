from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=680)
screen.bgcolor("black")
screen.title("Snakes")

start_position = [(0,0), (-20,0), (-40,0)]

for position in start_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)