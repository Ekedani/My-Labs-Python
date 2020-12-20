a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
if a > b or a < 1:
        print('Введите корректные начальные значения!')
else:
    for number in range(a, b+1):
        is_odd = True
        counter = 2
        while is_odd and counter < number:
            if number % counter == 0:
                is_odd = False
            counter += 1
        if is_odd and number != 1:
            print(number, ' - простое число')

