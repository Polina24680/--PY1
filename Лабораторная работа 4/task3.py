
 #TODO реализовать функцию удаления элемента из списка по индексу




def delete(list_, index=None):
    return list_[:index] + list_[index+1:]

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 5], index= 5))  # [0, 1, 2, 3]

