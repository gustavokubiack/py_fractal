from turtle import *

def fractal_turtle():
    hideturtle()
    penup()
    speed('fastest')
    pencolor('red')
    goto(-200, 100)
    pendown()

    for i in range(3):
        fractal(400, 5)
        right(120)
        i = i + 1

    penup()
    goto(0,0)
    pendown()

    begin_fill()
    for i in range (180):
        forward(i + 1)
        left(91)
        if i % 2 == 0:
            fillcolor('purple')
        else:
            fillcolor('blue')

    end_fill()

def fractal(length, depth):
    if depth == 0:
        forward(length)
    else:
        fractal(length / 3, depth - 1)
        left(60)
        fractal(length / 3, depth - 1)
        right(120)
        fractal(length / 3, depth - 1)
        left(60)
        fractal(length / 3, depth - 1)

def main():
    fractal_turtle()
    done()

if __name__ == "__main__":
    main()
