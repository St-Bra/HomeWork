import multiprocessing
import time
import threading

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def main():
    start = time.time()
    for offset in range(4):
        factorial(50000 + offset*500)
    end = time.time()
    print(f'Затраченное время в последовательной версии: {end - start:.1f} секунд')


def main_threading():
    threads = []
    start = time.time()
    for offset in range(4):
        t = threading.Thread(target=factorial, args=(50000 + offset * 500,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print(f'Затраченное время в многопоточной версии: {end - start:.1f} секунд')



def main_muiltiproc():
    processes = []
    start = time.time()
    for offset in range(4):
        p = multiprocessing.Process(target=factorial, args=(50_000 + offset * 500,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    print(f'Затраченное время в мультипроцессорной версии: {end - start:.1f} секунд')

if __name__ == "__main__":
    main()
    main_threading()
    main_muiltiproc()