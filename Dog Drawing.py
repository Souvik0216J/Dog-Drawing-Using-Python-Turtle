import turtle as turtle
# turtle.screensize(500, 500)
turtle.pensize(5)
turtle.home()
turtle.seth(0)
turtle.pd()  
turtle.color('black')
turtle.circle(20, 80)  
turtle.circle(200, 30)  
turtle.circle(30, 60)  
turtle.circle(200, 29.5)  
turtle.color('black')
turtle.circle(20, 60)  
turtle.circle(-150, 22)  
turtle.circle(-50, 10)  
turtle.circle(50, 70)  
x_nose = turtle.xcor()
y_nose = turtle.ycor()
turtle.circle(30, 62)  
turtle.circle(200, 15)  
turtle.pu() 
turtle.goto(x_nose, y_nose + 25)
turtle.seth(90)
turtle.pd()
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()
turtle.pu()
turtle.goto(x_nose + 48, y_nose + 55)
turtle.seth(90)
turtle.pd()
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()
turtle.pu()
turtle.color('#444444')
turtle.goto(x_nose + 100, y_nose + 110)
turtle.seth(182)
turtle.pd()
turtle.circle(15, 45)
turtle.color('black')
turtle.circle(10, 15)
turtle.circle(90, 70)
turtle.circle(25, 110)
turtle.rt(4)
turtle.circle(90, 70)
turtle.circle(10, 15)
turtle.color('#444444')
turtle.circle(15, 45)
turtle.pu()
turtle.color('black')
turtle.goto(x_nose + 90, y_nose - 30)
turtle.seth(-130)
turtle.pd()
turtle.circle(250, 28)
turtle.circle(10, 140)
turtle.circle(-250, 25)
turtle.circle(-200, 25)
turtle.circle(-50, 85)
turtle.circle(8, 145)
turtle.circle(90, 45)
turtle.circle(550, 5)
turtle.seth(0)
turtle.circle(60, 85)
turtle.circle(40, 65)
turtle.circle(40, 60)
turtle.lt(150)  
turtle.circle(-40, 90)
turtle.circle(-25, 100)
turtle.lt(5)
turtle.fd(20)
turtle.circle(10, 60)
turtle.rt(80)  
turtle.circle(200, 35)
turtle.pensize(20)
turtle.color('red')
turtle.lt(10)
turtle.circle(-200, 25)
turtle.pu()
turtle.fd(18)
turtle.lt(90)
turtle.fd(18)
turtle.pensize(6)
turtle.seth(35)  
turtle.color('blue')
turtle.begin_fill()
turtle.lt(135)
turtle.fd(6)
turtle.right(180)  
turtle.circle(6, -180)
turtle.backward(8)
turtle.right(90)
turtle.forward(6)
turtle.circle(-6, 180)
turtle.fd(15)
turtle.end_fill()
turtle.pensize(5)
turtle.pu()
turtle.color('black')
turtle.goto(x_nose + 100, y_nose - 125)
turtle.pd()
turtle.seth(-50)
turtle.fd(25)
turtle.circle(10, 150)
turtle.fd(25)
turtle.pensize(4)
turtle.pu()
turtle.goto(x_nose + 314, y_nose - 125)
turtle.pd()
turtle.seth(-95)
turtle.fd(25)
turtle.circle(-5, 150)
turtle.fd(2)
turtle.hideturtle()
turtle.done()