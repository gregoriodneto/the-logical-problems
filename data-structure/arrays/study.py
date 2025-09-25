# criando um “array” (lista em Python)
arr = [10, 20, 30, 40]
print(arr)  # [10, 20, 30, 40]

# acesso por índice
print(arr[0])  # 10
print(arr[2])  # 30

# modificar
arr[1] = 25
print(arr)  # [10, 25, 30, 40]

# inserir no fim
arr.append(50)
print(arr)  # [10, 25, 30, 40, 50]

# inserir no meio (posição 2)
arr.insert(2, 27)
print(arr)  # [10, 25, 27, 30, 40, 50]

# remover elemento em índice 3
x = arr.pop(3)
print("removido:", x)  # removido: 30
print(arr)  # [10, 25, 27, 40, 50]

# remover por valor (remove a primeira ocorrência)
arr.remove(27)
print(arr)  # [10, 25, 40, 50]

# checar existência
print(25 in arr)  # True
print(100 in arr)  # False

# buscar índice de valor
print(arr.index(40))  # e.g. 2

# iterar todos
for v in arr:
    print(v)
