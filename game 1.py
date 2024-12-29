from turtle import Turtle, Screen
window = Screen()
aya = Turtle()
window.title("aya: game")
list_shape = ["circle", "square", "triangle"]

def draw_square():
    for _ in range(4):
        aya.pensize(10)
        aya.color("red")
        aya.shape("turtle")
        aya.forward(100)
        aya.left(90)
def draw_triangle():
    for _ in range(3):
        aya.pensize(4)
        aya.color("purple")
        aya.shape("circle")
        aya.forward(200)
        aya.left(120)
def draw_circle():
    aya.pensize(8)
    aya.color("black")
    aya.shape("square")
    aya.circle(100)

game_on = True
while game_on:
    user_choice = window.textinput("wait", "choose between square, triangle, circle")
    if user_choice in list_shape:
        if user_choice == "square":
            draw_square()
        elif user_choice == "circle":
            draw_circle()
        else:
            draw_triangle()
    elif user_choice == "exit":
        game_on = False
        window.clear()
        aya.color("black")
        aya.hideturtle()
        window.bgcolor("orange")
        aya.write("press any click or key to exut", align="center", font= ("arial", 35, "normal"))
        aya.color("darkgray")
        aya.penup()
        aya.goto(0,-50)
        aya.pendown()
        

window.exitonclick()
