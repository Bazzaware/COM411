import matplotlib.pyplot as plt


def small():
    x_value = [3, 3, 3, 4, 4, 3]
    y_value = [3, 3, 4, 4, 3, 3]
    plt.plot(x_value, y_value, 'r:o')


def medium():
    x_value = [2, 2, 5, 5, 2]
    y_value = [2, 5, 5, 2, 2]
    plt.plot(x_value, y_value, 'g--s')


def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    plt.plot(x, y, 'b-p')


def run():
    small()
    medium()
    large()
    plt.show()


if __name__ == "__main__":
    run()
