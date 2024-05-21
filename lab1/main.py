import numpy as np
import random


def multVector():
    l1 = [10, 20, 30, 40, 50]
    l2 = [1, 2, 3, 4, 5]
    vector1 = np.array(l1)
    vector2 = np.array(l2)
    c = 0
    for i in range(len(vector1)):
        c += vector1[i] * vector2[i]
    print("Скалярное произведение векторов:", c)


def multMatrix():
    matrix1 = [[0] * 3 for _ in range(3)]
    matrix2 = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            matrix1[i][j] = random.randint(0, 100)
            matrix2[i][j] = random.randint(0, 100)

    matrix3 = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for t in range(3):
                matrix3[i][j] += matrix1[i][t] * matrix2[t][j]

    for i in range(3):
        for j in range(3):
            print(str(matrix1[i][j]) + ' ', end="")
        print('\t', end="")
        for j in range(3):
            print(str(matrix2[i][j]) + ' ', end="")
        print('\t', end="")
        for j in range(3):
            print(str(matrix3[i][j]) + ' ', end="")
        print()


def sortInsert():
    mas = [7, 8, 5, 9, 10, 4, 2, 1, 3, 6]
    b = 0
    print("Сортировка вставкой:")
    print(mas)
    for i in range(1, 10):
        b = mas[i]
        j = i - 1
        while (j >= 0 and b < mas[j]):
            mas[j + 1] = mas[j]
            j = j - 1
        mas[j + 1] = b

    print(mas)


def sortChoice():
    mas = [7, 8, 5, 9, 10, 4, 2, 1, 3, 6]
    mindex = 0
    min = 0
    b = 0
    print("Выбором:")
    print(mas)
    for i in range(0, 10):
        min = mas[i]
        mindex = i
        for j in range(i, 10):
            if mas[j] < min:
                min = mas[j]
                mindex = j
        b = mas[i]
        mas[i] = mas[mindex]
        mas[mindex] = b

    print(mas)


def sortBubble():
    mas = [7, 8, 5, 9, 10, 4, 2, 1, 3, 6]
    print("Пузыриком:")
    print(mas)
    for i in range(0, 9):
        swapped = False
        for j in range(0, 9 - i):
            if mas[j] > mas[j + 1]:
                b = mas[j]
                mas[j] = mas[j + 1]
                mas[j + 1] = b
                swapped = True
        if not swapped:
            break

    print(mas)


multVector()
multMatrix()
sortInsert()
sortChoice()
sortBubble()
