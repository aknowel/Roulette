
class RouletteAnalyzer(object):

    @staticmethod
    def divisible_by(numbers_list, n):
        result = list()
        for i in range(n):
            result.append([j for j in numbers_list if j % n == i])
        return result

    @staticmethod
    def jumped_divide_list(numbers_list, n):
        result = list()
        if len(numbers_list) % n != 0:
            return None
        for i in range(n):
            result.append([ j for j in numbers_list[ i : : n ] ])
        return result

    @staticmethod
    def consecutive_divide_list(numbers_list, n):
        result = list()
        if len(numbers_list) % n != 0:
            return None
        for i in range(n):
            result.append([ j for j in numbers_list[ i * (len(numbers_list) // n) : (i + 1) * (len(numbers_list) // n) ] ])
        return result

    @staticmethod
    def generate_from_config(config_dict):
        new_dict = dict()
        new_dict['numbers'] = sorted([i for i in range(int(config_dict['last']) + 1)])

        new_dict['reds'] = sorted([int(config_dict['reds'][i]) for i in range(len(config_dict['reds']))])
        new_dict['blacks'] = sorted([int(config_dict['blacks'][i]) for i in range(len(config_dict['blacks']))])
        new_dict['greens'] = sorted([int(config_dict['greens'][i]) for i in range(len(config_dict['greens']))])

        new_dict['numbers_without_greens'] = sorted([i for i in range(int(config_dict['last']) + 1) if i not in config_dict['greens']])

        result = RouletteAnalyzer.divisible_by(new_dict['numbers_without_greens'], 2)
        new_dict['evens'] = result[0]
        new_dict['odds'] = result[1]

        result = RouletteAnalyzer.consecutive_divide_list(new_dict['numbers_without_greens'], 2)
        new_dict['lowers'] = result[0]
        new_dict['highers'] = result[1]

        result = RouletteAnalyzer.consecutive_divide_list(new_dict['numbers_without_greens'], 3)
        new_dict['dozen1'] = result[0]
        new_dict['dozen2'] = result[1]
        new_dict['dozen3'] = result[2]

        result = RouletteAnalyzer.jumped_divide_list(new_dict['numbers_without_greens'], 3)
        new_dict['row1'] = result[0]
        new_dict['row2'] = result[1]
        new_dict['row3'] = result[2]
        return new_dict

    @staticmethod
    def consecutive_search(numbers: list, allowed: list, reverse=False):
        result = list()
        if not reverse:
            for i in numbers[::-1]:
                if i in allowed:
                    result.append(i)
                else:
                    break
        else:
            for i in numbers[::-1]:
                if i in allowed:
                    result.append(i)
                else:
                    break
        return result

    @staticmethod
    def shuffled_search(data_numbers_list, allowed_list_1, allowed_list_2, reverse=False):
        result = list()

        last_in_list_1 = False
        if data_numbers_list[-1] in allowed_list_1:
            last_in_list_1 = True
        elif data_numbers_list[-1] not in allowed_list_2:
            return result

        result.append(data_numbers_list[-1])

        if not reverse:
            for i in data_numbers_list[::-1]:
                if last_in_list_1:
                    if i in allowed_list_2:
                        result.append(i)
                        last_in_list_1 = False
                    else:
                        break
                else:
                    if i in allowed_list_1:
                        result.append(i)
                        last_in_list_1 = True
                    else:
                        break
        else:
            for i in data_numbers_list[::-1]:
                if last_in_list_1:
                    if i in allowed_list_2:
                        result.append(i)
                    else:
                        break
                else:
                    if i in allowed_list_1:
                        result.append(i)
                    else:
                        break
        return result
