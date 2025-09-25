def inverter_lista(arr):
    in_arr = []
    for i in range(len(arr) -1, -1, -1):
        in_arr.append(arr[i])
    return in_arr

print(inverter_lista([1, 2, 3, 4]))