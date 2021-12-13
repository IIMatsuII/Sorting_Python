def insertion_sort(alist): #Функция принимающая на вход список
    for i in range(1, len(alist)): #цикл с переменой i до длины списка - 1
        temp = alist[i] #Создаем переменую
        j = i - 1
        while (j >= 0 and temp < alist[j]): #Создадим цикл который будет работать до тех пор пока j не отрицательное и temp меньше чем элемент под индексом j
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = temp

alist = input("Enter the list of numbers: ").split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print("sorted list: ", end="")
print(alist)

"""
def insertion(data):
    for i in range(len(data))
        j = i + 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = key
    return data
"""