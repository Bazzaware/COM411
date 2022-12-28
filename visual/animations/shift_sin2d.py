import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

line = None


def animate(frame):
    global line
    x = range(0, 360)
    y = [math.sin(math.radians(degrees) + (frame / 50)) for degrees in x]
    line.set_data(x, y)


def run():
    global line
    fig, ax = plt.subplots()
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    line, = ax.plot([], [], linewidth=3)
    sine_animation = animation.FuncAnimation(fig,
                                             animate,
                                             frames=720,
                                             interval=100)
    plt.show()


run()