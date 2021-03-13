import random

l = [i for i in range(37)]

for i in range(1, 39):
    f = open('../data/generated/gen{}.txt'.format(i), 'w+')
    for j in range(500):
        f.write('{}\n'.format(random.choice(l)))
