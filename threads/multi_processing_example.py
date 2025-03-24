from ntpath import join
import time
import multiprocessing

# Criando uma variável global
results = []

def calc_square(numbers):
    global results
    for i in numbers:
        print('square: ', str(i * i))
        results.append(i * i)
        print('within a result: ' + str(results))

def calc_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print('cube: ', str(i * i * i))

if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2=join()
    print('result: ' + str(results))
    print('success')