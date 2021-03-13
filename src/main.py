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


handwritten_filepaths = ['../data/handwritten/list{}.txt'.format(i) for i in range(1, 39)]
generated_filepaths = ['../data/generated/gen{}.txt'.format(i) for i in range(1, 39)]

KFULL = 1000

config = Loader.load_config('config.json')
config = RouletteAnalyzer.generate_from_config(config)


vals = list()
vals.append(KFULL)
for _ in range(1000):
    l = Loader.random_sample(handwritten_filepaths, 100)
    K = 0.1 * KFULL
    KFULL -= K
    K = Simulator.simulate_bubbles_and_progression(l, config, K)[-1]
    KFULL += K
    vals.append(KFULL)

vals = [float(i) for i in vals]


def animation(i):
    plt.cla()
    plt.plot(vals[:i])
    if i < len(vals):
        plt.xlabel('K: {}    P/L: {}    I: {}'.format(vals[i], vals[i] - K, i))


#ani = FuncAnimation(plt.gcf(), animation, interval=10)
plt.plot(vals)
plt.show()
