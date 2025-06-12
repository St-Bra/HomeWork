import time
import threading
import multiprocessing
import requests

# URL, который отвечает с задержкой 1 секунда
urls = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(4)]

def get_url(url):
    response = requests.get(url)
    return response.status_code


def main_sequential():
    start = time.time()
    for url in urls:
        get_url(url)
    end = time.time()
    print(f"Последовательный запуск время выполнения: {end - start:.1f} секунд")


def main_threading():
    threads = []
    start = time.time()
    for url in urls:
        t = threading.Thread(target=get_url, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print(f"Многопоточный запуск время выполнения: {end - start:.1f} секунд")


def main_multiprocessing():
    processes = []
    start = time.time()
    for url in urls:
        p = multiprocessing.Process(target=get_url, args=(url,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    print(f"Мультипроцессный запуск время выполнения: {end - start:.1f} секунд")

if __name__ == "__main__":
    main_sequential()
    main_threading()
    main_multiprocessing()