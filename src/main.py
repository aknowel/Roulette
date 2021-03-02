from simulator import Simulator
from roulette import RouletteAnalyzer
from loader import Loader

from itertools import count
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

import numpy as np

import random
import colorama
colorama.init(autoreset=True)


handwritten_filepaths = ['../data/handwritten/list{}.txt'.format(i) for i in range(1, 23)]
generated_filepaths = ['../data/generated/gen{}.txt'.format(i) for i in range(1, 23)]

K = 100

config = Loader.load_config('config.json')
config = RouletteAnalyzer.generate_from_config(config)

vals = list()
for _ in range(10):
    l = Loader.random_sample(handwritten_filepaths, 100)
    vals += l

x_vals = [float(i) for i in Simulator.simulate_bubbles_and_progression(vals, config, K)]


def animation(i):
    plt.cla()
    plt.plot(x_vals[:i])
    if i < len(x_vals):
        plt.xlabel('K: {}    P/L: {}    I: {}'.format(x_vals[i], x_vals[i] - K, i))


ani = FuncAnimation(plt.gcf(), animation, interval=50)

plt.show()
