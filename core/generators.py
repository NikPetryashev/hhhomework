from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for i in range(N):
        yield randint(1, 100)

# написать генераторное выражение, которое делает то же самое
# numbers = range(3)
N = 3
gen2 = (randint(1, 100) for i in range(N))

if __name__ == '__main__':
    print('Генераторная фукция')
    g = gen(3)
    [print(next(g)) for x in range(3)]

    print('Генераторное выражение')
    g2 = gen2
    [print(next(g2)) for x in range(3)]
