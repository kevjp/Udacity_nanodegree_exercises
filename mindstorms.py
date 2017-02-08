import turtle, webbrowser, time

def screen():
    window = turtle.Screen()
    window.bgpic("landscape.gif")
##    draw_square(window)
##    draw_circle()
##    draw_triangle()
    draw_flower()
    window.exitonclick()

    
def draw_square(window):
    brad = turtle.Turtle()
##    webbrowser.open("https://www.youtube.com/v/WsptdUFthWI&list=PLwpFrtWg2EJFsZK90YBdU1PNei0Hfo0lb?start=11&end=25&autoplay=1")
##    time.sleep(3)
    brad.speed(10)
    window.register_shape("kev.gif")
    brad.shape("kev.gif")
    brad.color("red")
    for baring in range(0,360, 10):
           brad.setheading(baring)

           count=0
           while count < 4:
               brad.forward(100)
               brad.right(90)
               count += 1



##def draw_circle():
##    angie = turtle.Turtle()
##    angie.shape("triangle")
##    angie.color("blue")
##    angie.circle(100)
##    
##
##def draw_triangle():
##    brian = turtle.Turtle()
##    brian.shape("square")
##    brian.color("yellow")
##    value = 0
##    while value < 3:
##        brian.left(240)
##        brian.forward(150)
##        value += 1

def draw_flower():
    clive = turtle.Turtle()
    clive.shape("turtle")
    clive.color("yellow")

    for val in range(0,36):
        clive.right(175)
        clive.begin_fill()
        clive.forward(100)
        clive.right(15)
        clive.forward(100)
        clive.right(165)
        clive.forward(100)
        clive.right(15)
        clive.forward(100)
        clive.end_fill()

    clive.right(90)
    clive.forward(400)

 
    
screen()

    
