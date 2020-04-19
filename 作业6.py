def selection_sort(list):
    for i in range(len(list)-1):
      min = i
      for j in range(i + 1, len(list)):
        if list[j] > list[min]:
          min = j
      list[i], list[min] = list[min], list[i]
    return list

print(selection_sort([3, 6, 9, 1, 10, 4]))

