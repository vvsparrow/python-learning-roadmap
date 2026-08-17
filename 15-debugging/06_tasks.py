# Задача 6 
# Программа должна рассчитывать произведение элементов списка, но она
# возвращает неправильный результат или выдает ошибку. Необходимо найти и
# исправить ошибку в функции, используя отладчик debugger, чтобы она правильно
# рассчитывала произведение элементов списка.

def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * lst[i]
        return result

print(multiplylist([1, 2, 3, 4]))