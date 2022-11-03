import turtle
t=turtle.Turtle()
t.shape("turtle")
t.lt(45)
t.fd(141)
t.setheading(0)
t.goto(0,0)
t.fd(100)
t.lt(90)
t.fd(100)

import math
x1=int(input("x1의 값: ")) #변수 x1의 값을 사용자로부터 받는다. int형으로
y1=int(input("y1의 값: ")) #변수 y1의 값을 사용자로부터 받는다. int형으로
x2=int(input("x2의 값: ")) #변수 x2의 값을 사용자로부터 받는다. int형으로
y2=int(input("y2의 값: ")) #변수 y2의 값을 사용자로부터 받는다. int형으로
import math
dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("두점 사이의 거리=",dist,"입니다.")

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.lt(45)
t.fd(141)
t.write("점의 길이"+str(dist))
