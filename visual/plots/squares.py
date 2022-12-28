import matplotlib.pyplot as plt


def small():
    # x_value = list().append(3, 4)
    # y_value = list().append(4, 4)
    x_value = [3, 3, 3, 4, 4, 3]
    y_value = [3, 3, 4, 4, 3, 3]
    plt.plot(x_value, y_value, "ro--")
    plt.show()


def run():
    small()


if __name__ == "__main__":
    run()
