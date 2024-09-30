import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=100):
    window = turtle.Screen()
    window.bgcolor("black")

    t = turtle.Turtle()
    t.color("red")
    t.speed(0)
    t.penup()
    t.goto(-size / 4, size/4)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()


level_recursion = int(input("Введіть рівень рекурсії:"))
draw_koch_curve(level_recursion)
