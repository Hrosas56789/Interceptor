'''
Hector Rosas
18/8/21
turtle stuff
'''

import turtle


wn = turtle.Screen()
wn.title("Tony monty")

tony = turtle.Turtle()

def k1():
    tony.forward(50)
def k2():
    tony.left(50)
def k3():
    tony.right(50)
def k4():
    tony.back(50)
wn.onkeypress(k1, "Up" or "w")
wn.onkeypress(k2, "Left" or "a")
wn.onkeypress(k3, "Right" or "d")
wn.onkeypress(k4, "Down" or "a")
wn.listen()


wn.mainloop()