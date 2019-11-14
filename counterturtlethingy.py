import turtle





def ninjaStar(x, y):
    turtle.color ('green')
    counter = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pd()
    while counter < 20:
        turtle.speed(900000)
        turtle.forward(90)
        turtle.forward(78)
        turtle.left(45)
        turtle.right(62)
        turtle.back(45)
        turtle.right(20)
        turtle.forward(78)
        turtle.left(45)
        turtle.right(62)
        turtle.color ('orange')
        turtle.back(45)
        turtle.forward(78)
        turtle.left(45)
        turtle.right(62)
        turtle.back(45)
        turtle.right(20)
        turtle.right(20)
        turtle.forward(78)
        turtle.left(45)
        turtle.right(62)
        turtle.back(45)
        turtle.right(20)
        turtle.color ('purple')
        turtle.right(70)
        turtle.color ('red')
        turtle.forward(25)
        turtle.color ('purple')
        turtle.forward(25)
        turtle.color ('yellow')
        turtle.forward(25)
        turtle.color ('green')
        turtle.forward(25)
        turtle.color ('orange')
        turtle.forward(25)
        turtle.color ('black')
        turtle.forward(25)
        counter = counter+1
    print(counter)

ninjaStar(100, 100)

ninjaStar(-100, -100)
