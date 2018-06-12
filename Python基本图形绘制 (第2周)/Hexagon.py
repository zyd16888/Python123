import turtle as t
t.setup(600,400,200,200)
t.penup()
t.seth(135)
t.fd(120)
t.pendown()
t.pensize(5)
t.seth(0)
for i in range(6):
    t.fd(120)
    t.right(60)
t.done()