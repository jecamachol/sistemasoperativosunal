import turtle
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("192.168.0.4", 5000)
sock.bind(address)
data, address = sock.recvfrom(256)

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("orange")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

def movement():

    if acelerometro_z > 5:
        head.direction == "up"
        y = head.ycor()
        head.sety(y + 10)
    elif acelerometro_z < -5:
        head.direction == "down"
        y = head.ycor()
        head.sety(y - 10)
    elif acelerometro_x < -5:
        head.direction == "right"
        x = head.xcor()
        head.setx(x + 10)
    elif acelerometro_x > 5:
        head.direction == "left"
        x = head.xcor()
        head.setx(x - 10)


while True:
    data, address = sock.recvfrom(256)
    acelerometro_x = float(data[17:24])
    acelerometro_z = float(data[33:40])
    print(acelerometro_x, " ", acelerometro_z)
    wn.update()
    movement()

    
