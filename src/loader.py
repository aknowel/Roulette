import colorama
import json
import random

class Loader(object):

    @staticmethod
    def check_config_file(config_dict):
        numbers = [i for i in range(int(config_dict['last']) + 1)]
        reds = [int(config_dict['reds'][i]) for i in range(len(config_dict['reds']))]
        blacks = [int(config_dict['blacks'][i]) for i in range(len(config_dict['blacks']))]
        greens = [int(config_dict['greens'][i]) for i in range(len(config_dict['greens']))]

        result = True

        for i in numbers:
            if not (i in reds or i in blacks or i in greens):
                print(colorama.Fore.RED + 'Tell me if {} is red or black or casino or change "last" in config'.format(i))
                result = False

        for i in reds:
            if not i in numbers:
                print(colorama.Fore.RED + '{} is in reds but not in range 0 - {}'.format(i, max(numbers)))
                result = False
            if i in blacks:
                print(colorama.Fore.RED + '{} cannot be both red and black'.format(i))
                result = False
            if i in greens:
                print(colorama.Fore.RED + '{} cannot be both red and casino'.format(i))
                result = False

        for i in blacks:
            if not i in numbers:
                print(colorama.Fore.RED + '{} is in blacks but not in range 0 - {}'.format(i, max(numbers)))
                result = False
            if i in greens:
                print(colorama.Fore.RED + '{} cannot be both black and casino'.format(i))
                result = False

        for i in greens:
            if not i in numbers:
                print(colorama.Fore.RED + '{} is in greens but not in range 0 - {}'.format(i, max(numbers)))
                result = False

        if result:
            print(colorama.Fore.GREEN + 'All parameters OK')

        return result

    @staticmethod
    def load_config(config_filepath):
        if isinstance(config_filepath, str):
            try:
                with open(config_filepath, 'r') as config_file:
                    config_dict = json.loads(config_file.read())
                    if Loader.check_config_file(config_dict):
                        return config_dict
            except FileNotFoundError as e:
                print(colorama.Fore.RED + '{} no such config file exists'.format(e.filename))
        else:
            print(colorama.Fore.RED + 'Pass string instead of {}'.format(type(config_filepath)))

    @staticmethod
    def check_data_numbers_list(data_numbers_list, config_dict):
        numbers = config_dict['numbers']
        result = True
        for i in data_numbers_list:
            if not i in numbers:
                print(colorama.Fore.RED + '{} is in file but not in range 0 - {}'.format(i, max(numbers)))
                result = False
        return result

    @staticmethod
    def load_data(filepath: str, config_dict: dict, reverse=False):
        try:
            with open(filepath, 'r') as data_file:
                data = data_file.read().split()
                data_numbers_list = [int(i) for i in data]
                if Loader.check_data_numbers_list(data_numbers_list, config_dict):
                    if reverse:
                        data_numbers_list = data_numbers_list[::-1]
                    else:
                        data_numbers_list = data_numbers_list
                    return data_numbers_list
        except FileNotFoundError as e:
            print('{} no such file exists'.format(e.filename))

    @staticmethod
    def random_sample(filepaths: list, samples_length: int) -> list:
        sample = random.choice(filepaths)
        with open(sample, 'r') as f:
            d = f.read().split()
            d = [int(i) for i in d]
            if len(d) < samples_length:
                print(colorama.Fore.RED + 'File too short')
            else:
                r = random.choice(range(len(d) - samples_length + 1))
                print(colorama.Fore.YELLOW + '{} {}:{}'.format(sample, r + 1, r + samples_length))
                return d[r : r + samples_length]
