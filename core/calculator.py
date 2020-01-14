from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation in ('+', '-', '/', '*', '**'):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '**':
            return a ** b
        elif operation == '/':
            if b != 0:
                return a / b
            else:
                print('Деление на 0 невозможно')
    else:
        print('Оператор \'' + operation + '\' некорректен')


if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
    except ValueError:
        print('Введены некорреткные значения')
    else:
        operation = input('Введите операцию: ')
        print('Результат: ', calculator(a, b, operation))

    print(calculator(5, 6, '+'))
    print(calculator(5, 6, '-'))
    print(calculator(5, 6, '+'))