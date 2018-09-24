def MinOfPlus():
    m, n = map(int, input("Введите размерность MxN через пробел: ").split())
    array = list()

    print("Введите строки матрицы через пробел: ")
    for _ in range(int(n)):
        array.append(list(map(int, input().split())))

    print("Матрица: ")
    for u in range(m):
        print(array[u])

    print("Результат: ")
    for i, m in enumerate(array):
        for j, n in enumerate(array):
            print(min(filter(lambda x: x > 0, array[i])))
            break


MinOfPlus()