import threading
import time
from concurrent.futures import ThreadPoolExecutor

N_ITER = 50_000_000
N_THREAD = 10

# thread run
def thread_run():
    count_thread = 0
    lock = threading.Lock()

    def increment_count(value: int):
        nonlocal count_thread
        with lock:
            for _ in range(value):
                count_thread += 1

    threads = [
        threading.Thread(target=increment_count, args=(N_ITER//N_THREAD,)) for _ in range(N_THREAD)
    ]

    start = time.perf_counter()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    perf_time = time.perf_counter() - start
    print(f"Thread running time is {perf_time:.5f}, count is {count_thread}")

# sequential run
def sequential_run():
    def increase_count():
        sequential_count = 0
        for _ in range(N_ITER):
            sequential_count += 1
        return sequential_count
    start = time.perf_counter()
    cnt = increase_count()
    time_perf = time.perf_counter() - start
    print(f"sequential running time is {time_perf:.5f}, count is {cnt}")


thread_run()
sequential_run()

"""
result is :

Thread running time is 1.70026, count is 50000000
sequential running time is 1.57385, count is 50000000

why this happened?:

the remaining timing differences are due to how CPython treats and optimizes global vs. local variables. 

tip how to speed up code? :

It looks like global variables are slower, thus avoid using them as much as possible and encapsulate your code into functions.
"""
