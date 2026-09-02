# Задача 4
# Напишите крайне невежливую программу, которая не позволяет
# пользователю выйти из неё в консоли с помощью KeyboardInterrupt. Будьте
# осторожны! Подсказка. Используйте рекурсию.


def roly_poly_toy():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Ты встрял чувачок!)")
        roly_poly_toy()


roly_poly_toy()
