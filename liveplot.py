import tkinter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import random
import collections
import numpy as np

matplotlib.use('TkAgg')
values_per_second = 50
seconds_to_plot = 4
entry_count = values_per_second * seconds_to_plot
data = collections.deque(maxlen=entry_count)
mean = collections.deque(maxlen=entry_count)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title("Random noise")

def main():
    plt.ion()
    plt.show()
    while True:
        plt.pause(0.01)
        data.append(random.random())
        plt.clf()
        plt.plot(data)
        plt.draw()


def animate(i):
    data.append(random.random())
    mean.append(sum(data) / len(data))
    #xs = [-x for x in range(len(data))]
    xs = np.linspace(-seconds_to_plot, 0, entry_count)
    ax1.clear()
    if len(data) < entry_count:
        ax1.plot(xs[-len(data):], data, label="Noise label", color='blue')
        ax1.plot(xs[-len(data):], mean, color='red')
    else:
        ax1.plot(xs, data, label="Noise label", color='blue')
        ax1.plot(xs, mean, color='red')
    plt.xlabel("time [s]")
    plt.ylabel("angle [°]")
    ax1.legend()


def animate_example(i):
    xs = []
    ys = []
    for x in range(10):
        y = random.random()
        xs.append(float(x))
        ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


#ani = animation.FuncAnimation(fig, animate_example, interval=100)
ani = animation.FuncAnimation(fig, animate, interval=(1000 / values_per_second))
plt.show()
