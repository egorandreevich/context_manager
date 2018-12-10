import time
start_time = time.time()


class Timer():
    def __enter__(self):
        print('Время начала работы программы {}'.format(time.ctime(start_time)))
        return

    def __exit__(self, type, value, traceback):
        print('Файл test.txt с расчетным количеством водки записан.\nСчастливого Нового года!')
        print('Время окончания работы программы {}'.format(time.ctime(time.time())))
        print("Работа программы заняла %s секунд" % (time.time() - start_time))
        # return isinstance(value, TypeError)


with Timer() as thing:
    with open('test.txt', 'wt', encoding='utf-8') as f:
        def vodka_liters():
            print('Делим количество водки на человека.\nВведите, сколько у вас есть литров:')
            num = float(input())
            print('Сколько вас человек?')
            people = int(input())
            vodka_per_person = num / people
            return ('Каждому по: {} литру/литра'.format(vodka_per_person))

        try:
            f.write(vodka_liters())
        except ValueError:
            print('Значение не является числом')
