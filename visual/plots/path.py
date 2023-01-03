import matplotlib.pyplot as plt


def coordinate() -> dict:
    plots = dict()
    x_value = input('Enter a value for x')
    y_value = input('Enter a value for y')
    plots['x_value'] = x_value
    plots['y_value'] = y_value
    return plots


def path() -> None:
    print('retieving path ...')
    x_values = list()
    y_values = list()
    loop = 1
    while loop <= 4:
        data = coordinate()
        for key, value in data.items():
            if key == 'x_value':
                x_values.append(value)
            elif key == 'y_value':
                y_values.append(value)
        loop += 1

    return list((x_values, y_values))


def run() -> None:
    values = path()
    x = list()
    y = list()

    for value in values:
        x.append(value[0])
        y.append(value[1])
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    run()
