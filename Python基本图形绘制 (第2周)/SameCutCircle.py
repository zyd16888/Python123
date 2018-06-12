import turtle as t
t.setup(600,400,200,200)
t.pensize(5)
t.penup()
t.seth(-90)
t.fd(160)
t.pendown()
t.seth(0)
r = 20
for i in range(5):
    t.circle(r, 360)
    r = r + 20
t.done()