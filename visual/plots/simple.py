import matplotlib.pyplot as plt


def display(x_value, y_value):
    plt.plot(x_value,y_value)
    breakpoint()
    plt.show()



def run():
    x_value = [1, 2, 3, 4, 5]
    y_value = [1, 4, 9, 16, 25]
    display(x_value, y_value)


run()
