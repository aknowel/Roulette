from roulette import RouletteAnalyzer

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
                    K += b / 2

                elif n[-1] in g:
                    K += b * (len(config['numbers_without_greens']) / len(g))

            result.append(K)

            bets.clear()

            reds = RouletteAnalyzer.consecutive_search(n, config['reds'])
            blacks = RouletteAnalyzer.consecutive_search(n, config['blacks'])
            lowers = RouletteAnalyzer.consecutive_search(n, config['lowers'])
            highers = RouletteAnalyzer.consecutive_search(n, config['highers'])
            evens = RouletteAnalyzer.consecutive_search(n, config['evens'])
            odds = RouletteAnalyzer.consecutive_search(n, config['odds'])
            
            v1 = 2

            if len(reds) == v1:
                bets.append((config['blacks'], 0.01 * K))
            elif len(reds) == v1 + 1:
                bets.append((config['blacks'], 0.02 * K))


            if len(blacks) == v1:
                bets.append((config['reds'], 0.01 * K))
            elif len(blacks) == v1 + 1:
                bets.append((config['reds'], 0.02 * K))



            if len(lowers) == v1:
                bets.append((config['highers'], 0.01 * K))
            elif len(lowers) == v1 + 1:
                bets.append((config['highers'], 0.02 * K))



            if len(highers) == v1:
                bets.append((config['lowers'], 0.01 * K))
            elif len(highers) == v1 + 1:
                bets.append((config['lowers'], 0.02 * K))



            if len(evens) == v1:
                bets.append((config['odds'], 0.01 * K))
            elif len(evens) == v1 + 1:
                bets.append((config['odds'], 0.02 * K))


            
            if len(odds) == v1:
                bets.append((config['evens'], 0.01 * K))
            elif len(odds) == v1 + 1:
                bets.append((config['evens'], 0.02 * K))

            if K >= 2 * K_begin or K < K_begin / 10:
                break
            
        return result
            