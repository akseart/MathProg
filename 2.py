u"""
Решение задачи линейного программирования методом симплекс метода
Составление двойственной задачи и её решение вариант 23
"""
import numpy


def func(X):
    return -2*X[1]-X[2]+X[6]


def source():
    Z = numpy.array([-2, -1, 0, 0, 0, 1], float)
    X = numpy.array([[1, 2, 1, 1, 0, 0],
                     [-1, -1, 0, 0, 1, 0],
                     [1, -1, -1, 0, 0, 1]], float)
    B = numpy.array([6, 1, 4], float)
    # Нахождение базисных элеметов
    base = numpy.array([4, 5, 6], int)
    return Z, X, B, base


# inp - двумерный массив
def simplex_method1(inp):
    table = numpy.empty([len(inp), len(inp) + len(inp[0]) - 1], dtype=float)
    basis = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if (j < len(inp[i])):
                table[i, j] = inp[i, j]
            else:
                table[i, j] = 0
            if ((len(inp[i]) + i) < len(inp[i])):
                table[i, len(inp[i])+i] = 1
                basis.append(len(inp[i])+i)
    leadColumn = -1
    leadline = -1
    while not isItEnd(table):
        for j in range(2, len(table[0])):
                if (table[len(table) - 1, j] < table[len(table) - 1, leadColumn]):
                    leadColumn = j
        for i in range(len(table) - 1):
                    if (table[i, leadline] > 0):
                        leadline = i
                        break
        for i in range(leadline + 1, len(table) - 1):
            if ((table[i, leadline] > 0) and
                ((table[i, 0] / table[i, leadline]) <
                (table[leadline, 0] / table[leadline, leadColumn]))):
                leadColumn = i
        basis[leadline] = leadColumn
        new_table = numpy.empty([len(inp), len(inp[0])], dtype=float)
        for j in range(len(table[0])):
            new_table = numpy.empty([len(inp), len(inp) + len(inp[0]) - 1], dtype=float)
            new_table[leadline, j] = table[leadline, j] / table[leadline, leadColumn]
        for i in range(len(table)-1):
            if (i == leadline):
                continue
            for j in range(len(table[0])):
                new_table[i, j] = table[i, j] - table[i, leadColumn] * new_table[leadline, j]
        table = new_table
    result = []
    for i in len(result):
            k = basis.IndexOf(i + 1)
            if (k != -1):
                result.append(table[k, 0])
            else:
                result.append(0)
    return table, result


def isItEnd(table):
    flag = True
    for i in range(len(table[0])-1):
        if (table[len(table)-1, i] < 0):
            flag = False
    return flag


def simplex_method(inp):
    Z, X, B, base = inp()
    # Выбор ведущего столбца
    leadColumn = numpy.argmin(Z)
    # Нахождение симплекс отношений
    simplexRelations = leadColumn.copy()
    # Выбор ведущей строки
    leadline = -1
    for i in range(simplexRelations.len()):
        if (X[leadColumn][i] == 0):
            simplexRelations[i] = 0
        else:
            simplexRelations[i] = B[i]/X[leadColumn][i]
            if ((simplexRelations[i] < simplexRelations[leadline]
                 and simplexRelations[i] > 0) or leadline == -1):
                leadline = i
    # Проверка на существования задачи
    if (leadline == -1):
        print("Задача не имеет решения :(")
        return
    # Выбор ведущего элемента
    Xnew = X.copy()
    Znew = Z.copy()
    Bnew = B.copy()
    Xnew.fill(0)
    Znew.fill(0)
    Bnew.fill(0)
    # Переход к новой таблице
    # Вычисление ведущей строки
    for i in range(X.shape[1]):
        Xnew[leadline][i] = X[leadline][i] / X[leadline][leadColumn]


# Правило прямоугольника
inp = numpy.array([[1, 1, 1, -1],
                  [0, 3, -1, -1],
                  [-1, 3, -1, 2],
                  [0, -6, -4, -1]], float)
# simplex_method1(sourcee)

table = numpy.empty([len(inp), len(inp) + len(inp[0]) - 1], dtype=float)
basis = []
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if (j < len(inp[i])):
            table[i, j] = inp[i, j]
        else:
            table[i, j] = 0
    if ((len(inp[i]) + i) < len(table[0])):
        table[i, len(inp[i])+i] = 1
        basis.append(len(inp[i])+i)
        print("{EQ}")
leadColumn = -1
leadline = -1
print(basis)
while not isItEnd(table):
    for j in range(2, len(table[0])):
            if (table[len(table) - 1, j] < table[len(table) - 1, leadColumn]):
                leadColumn = j
    for i in range(len(table) - 1):
                if (table[i, leadline] > 0):
                    leadline = i
                    break
    for i in range(leadline + 1, len(table) - 1):
        if ((table[i, leadline] > 0) and
            ((table[i, 0] / table[i, leadline]) <
            (table[leadline, 0] / table[leadline, leadColumn]))):
            leadColumn = i
    basis[leadline] = leadColumn
    new_table = numpy.empty([len(inp), len(inp[0])], dtype=float)
    for j in range(len(table[0])):
        new_table = numpy.empty([len(inp), len(inp) + len(inp[0]) - 1], dtype=float)
        new_table[leadline, j] = table[leadline, j] / table[leadline, leadColumn]
    for i in range(len(table)-1):
        if (i == leadline):
            continue
        for j in range(len(table[0])):
            new_table[i, j] = table[i, j] - table[i, leadColumn] * new_table[leadline, j]
    table = new_table
result = []
basis
for i in range(len(inp)-1):
    if basis.count(i+1) == 0:
        result.append(0)
    else:
        k = basis.index(i + 1)
        result.append(table[k, 0])
print(result)
result
