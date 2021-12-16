#Создадим функцию heapsort, которая принимает на вход список.
def heapsort(alist):
    # Вызовем функцию build_max_heap c параметром alist для представления листа в виде пирамиды (heap).
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        # Поменяем местами первый и последний элемент пирамиды.
        alist[0], alist[i] = alist[i], alist[0]
        # Вызовем функцию max_heapify, учитывая что новая пирамида имеет размер на единицу меньше. Установим index=0 для удовлетворения параметрам пирамиды.
        max_heapify(alist, index=0, size=i)
        # Повторим шаги 3 и 4, пока размер пирамиды не станет 0 и весь список не отсортируется.




#Определим функцию parent, которая принимает index и возвращает индекс родителя.
def parent(i):
    return(i - 1)//2

#Определим функцию left, которая принимает index и возвращает индекс левого дочернего элемента.
def left(i):
    return 2*i+1

#Определим функцию right, которая принимает index и возвращает индекс правого дочернего элемента.
def right(i):
    return 2*i+2

#Определим функцию build_max_heap, которая принимает список аргументов и переставляет их в соостветсвии с max heap.
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start -= 1
#build_max_heap вызывает max_heapify на каждом родительском ноде и проходит до вершины.
def max_heapify(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start -= 1

#Определим функцию max_heapify, которая принимает индекс и изменяет структуру пирамиды на ноде и снизу от индекса так, чтобы удовлетворять правилам пирамиды.
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index

    if(r < size and alist[r] > alist[largest]):
        largest = r

    if (largest!= index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)

alist = input("Enter the list of numbers:").split()
alist = [int(x) for x in alist]
heapsort(alist)
print("Sotrted list:", end = "")
print(alist)
