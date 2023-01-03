import matplotlib.pyplot as plt


def line():
    x = [0, 2, 4, 6, 8, 10]
    y = [0, 20, 40, 60, 80, 100]

    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.plot(x, y)
    plt.show()


def dot():
    x = [0, 2, 4, 6, 8, 10]
    y = [0, 20, 40, 60, 80, 100]

    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.plot(x, y, "o")
    plt.show()


def step():
    x = [0, 2, 4, 6, 8, 10]
    y = [0, 20, 40, 60, 80, 100]

    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.step(x, y)
    plt.show()


line()
dot()
step()
