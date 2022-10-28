def iteration_1(x):
    return x % 2 == 0


for i in range(10):
    if iteration_1(i):
        print([i])
    else:
        print([False])


def iteration_2(x):
    return x % 2 == 0


print([i if iteration_2(i) else False for i in range(10)])
