import time

start_time = time.time()
print('Время начала работы программы {}'.format(time.ctime(start_time)))

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


print('Время окончания работы программы {}'.format(time.ctime(time.time())))
print("Работа программы заняла %s секунд" % (time.time() - start_time))
