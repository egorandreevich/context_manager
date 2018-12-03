import time

start_time = time.time()
print('Время начала работы программы {}'.format(time.ctime(start_time)))
with open('test.txt', 'wt', encoding='utf-8') as f:
    num = int(input())
    line = str('1/' + str(num) + '=' + str(1/num))
    print(line)
    f.write(line)


# main()
print('Время окончания работы программы {}'.format(time.ctime(time.time())))
print("Работа программы заняла %s секунд" % (time.time() - start_time))