from roulette import RouletteAnalyzer
from math import ceil
import random
import colorama

class Simulator(object):


    @staticmethod
    def simulate_bubbles_and_progression(numbers: list, config: dict, K: int) -> list:
        K_begin = K
        result = list()
        bets = list()
        for i in range(len(numbers)):
            n = numbers[:i]

            for g, b in bets:
                K -= b

                if n[-1] in config['greens']:
                    K += (b / 2)

                elif n[-1] in g:
                    K += b * (len(config['numbers_without_greens']) / len(g))

            result.append(K)

            bets.clear()

            v1 = 2

            l = [('reds', 'blacks'),
                ('blacks', 'reds'),
                ('lowers', 'highers'),
                ('highers', 'lowers'),
                ('evens', 'odds'),
                ('odds', 'evens')]
            

            for x, y in l:
                if len(RouletteAnalyzer.consecutive_search(n, config[x])) == v1:
                    bets.append((config[y], 0.01 * K))
                elif len(RouletteAnalyzer.consecutive_search(n, config[x])) == v1 + 1:
                    bets.append((config[y], 0.03 * K))


            if K >= 2 * K_begin or K < K_begin / 10:
                break
            
        return result
