def MinOfPlus():
    m, n = map(int, input("Введите размерность MxN через пробел: ").split())
    array = []

    print("Вводите елементы через Enter: ")
    for i in range(m):
        array.append([])
        for j in range(n):
            array[i].append(input())

    print("Матрица: ")
    for u in range(m):
        print(array[u])

    print("Результат: ")
    for i in range(m):
        for j in range(n):
            print(min(array[i]))
            break


MinOfPlus()