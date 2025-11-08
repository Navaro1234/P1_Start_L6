import turtle

aantal_punten = input("Hoeveel punten moet de ster hebben? ")
aantal_punten = int(aantal_punten)

t = turtle.Turtle()
t.speed(100)

for i in range(aantal_punten):
    if i % 2 == 0:
        t.color("red")
    else:
     t.color("blue")

    t.forward(200)
    t.right(180 - 180 / aantal_punten)

t.hideturtle()
turtle.done()
