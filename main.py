from graphics import *
import random
import numpy as np

win = GraphWin('SCORE 4', 1000, 700)  # give title and dimensions
for o in range(0, 700, 100):
    line = Line(Point(00, o), Point(700, o))
    line.draw(win)
for o in range(0, 800, 100):
    line = Line(Point(o, 0), Point(o, 600))
    line.draw(win)


def main(tetagmenh, tetmhmenh, xroma):
    head = Circle(Point(tetmhmenh, tetagmenh), 40)  # set center and radius
    head.setFill(xroma)
    head.draw(win)


assoi = 0
dyaria = 0
A = np.arange(42).reshape(6, 7)
for x in range(0, 6):
    for y in range(0, 7):
        A[x, y] = 0
print(A)
print("=================================")

for v in range(0, 22):
    p = win.getMouse()
    x = int(p.x)
    a = x // 100
    if A[0, a] == 0:
        if A[1, a] == 0:
            if A[2, a] == 0:
                if A[3, a] == 0:
                    if A[4, a] == 0:
                        if A[5, a] == 0:
                            A[5, a] = 1
                            main(5 * 100 + 50, a * 100 + 50, "red")
                            print(1)
                        else:
                            A[4, a] = 1
                            main(4 * 100 + 50, a * 100 + 50, "red")
                    else:
                        A[3, a] = 1
                        main(3 * 100 + 50, a * 100 + 50, "red")
                else:
                    A[2, a] = 1
                    main(2 * 100 + 50, a * 100 + 50, "red")
            else:
                A[1, a] = 1
                main(1 * 100 + 50, a * 100 + 50, "red")
        else:
            A[0, a] = 1
            main(0 * 100 + 50, a * 100 + 50, "red")
    else:
        print("λαθος")
    print(A)
    for y in range(0, 6):
        for x in range(0, 4):
            if A[y, x] == A[y, x + 1] == A[y, x + 2] == A[y, x + 3] == 1:
                print("κερδισε ο παικτης Νο 1")
                raise SystemExit(0)
            if x == 3:
                continue
            if A[x, y] == A[x + 1, y] == A[x + 2, y] == A[x + 3, y] == 1:
                print("κερδισε ο παικτης Νο 1")
                raise SystemExit(0)
    for x in range(0, 6):
        for y in range(0, 7):
            if y + 3 < 7 and x + 3 < 6:
                if A[x, y] == A[x + 1, y + 1] == A[x + 2, y + 2] == A[x + 3, y + 3] == 1:
                    print("κερδισε ο παικτης Νο 1")
                    raise SystemExit(0)
            if y - 3 > -1 and x + 3 < 6:
                if A[x, y] == A[x + 1, y - 1] == A[x + 2, y - 2] == A[x + 3, y - 3] == 1:
                    print("κερδισε ο παικτης Νο 1")
                    raise SystemExit(0)
    print("=================================")
    p = win.getMouse()
    x = int(p.x)
    a = x // 100
    if A[0, a] == 0:
        if A[1, a] == 0:
            if A[2, a] == 0:
                if A[3, a] == 0:
                    if A[4, a] == 0:
                        if A[5, a] == 0:
                            A[5, a] = 2
                            main(5 * 100 + 50, a * 100 + 50, "yellow")
                        else:
                            A[4, a] = 2
                            main(4 * 100 + 50, a * 100 + 50, "yellow")
                    else:
                        A[3, a] = 2
                        main(3 * 100 + 50, a * 100 + 50, "yellow")
                else:
                    A[2, a] = 2
                    main(2 * 100 + 50, a * 100 + 50, "yellow")
            else:
                A[1, a] = 2
                main(1 * 100 + 50, a * 100 + 50, "yellow")
        else:
            A[0, a] = 2
            main(0 * 100 + 50, a * 100 + 50, "yellow")
    else:
        print("λαθος")
        break
    # print(A[5, 6])
    for y in range(0, 6):
        for x in range(0, 4):
            print(A[y, x], A[y, x + 1], A[y, x + 2], A[y, x + 3])
            if A[y, x] == A[y, x + 1] == A[y, x + 2] == A[y, x + 3] == 2:
                print("κερδισε ο παικτης Νο 2")
                raise SystemExit(0)
            if x == 3:
                continue
            if A[x, y] == A[x + 1, y] == A[x + 2, y] == A[x + 3, y] == 2:
                print("κερδισε ο παικτης Νο 2")
                raise SystemExit(0)
    for x in range(0, 6):
        for y in range(0, 7):
            if y + 3 < 7 and x + 3 < 6:
                if A[x, y] == A[x + 1, y + 1] == A[x + 2, y + 2] == A[x + 3, y + 3] == 2:
                    print("κερδισε ο παικτης Νο 2")
                    raise SystemExit(0)
            if y - 3 > -1 and x + 3 < 6:
                if A[x, y] == A[x + 1, y - 1] == A[x + 2, y - 2] == A[x + 3, y - 3] == 2:
                    print("κερδισε ο παικτης Νο 2")
                    raise SystemExit(0)
    print("=================================")
