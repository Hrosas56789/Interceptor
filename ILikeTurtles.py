'''
Hector Rosas
18/8/20

Using turtle module
'''

import turtle

window = turtle.Screen()

vito = turtle.Turtle()

vito.onkey()
vito.setup(500,500)
wn = turtle.Screen()
wn.title("Turtle Keys")
move = turtle.Turtle()
def k1():
    move.forward(10)
def k2():
    move.left(10)
def k3():
    move.right(10)
def k4():
    move.back(10)
wn.onkeypress(k1, "Up")
wn.onkeypress(k2, "Left")
wn.onkeypress(k3, "Right")
wn.onkeypress(k4, "Down")
wn.listen()



window.mainloop()

