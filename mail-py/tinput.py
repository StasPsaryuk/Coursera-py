def t_input():
    while (True):
        try:
            a, b, c = map(int, input("Введіть змінні: ").split())
        except Exception:
            print('Введено більше/менше 3-х змінних!')
        else:
            print(a, b, c)
            break
t_input()

#
# Введення 3-х змінних, та перевірка
# кількості введених змінних.
#
#