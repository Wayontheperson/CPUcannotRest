"""
Thread order is unpredictable

When you use a thread/process/whatever pool, the work will be done in an arbitrary order

but when you want to make it in order, how to control the return value's order?
"""
import threading
import time

lock = threading.Lock()


def task1():
    time.sleep(.5)
    print("하나")
    return "하나"


def task2():
    time.sleep(.5)
    print("둘")
    return "둘"


def task3():
    time.sleep(.5)
    print("셋")
    return "셋"


def task4():
    time.sleep(.5)
    print("야")
    return "야"


th1 = threading.Thread(target=task1)
th2 = threading.Thread(target=task2)
th3 = threading.Thread(target=task3)
th4 = threading.Thread(target=task4)

th4.start()
th3.start()
th2.start()
th1.start()
# result is 야셋하나둘. it is unpredictable

time.sleep(2)  # for thread finished

# First answer
# use join
print("First answer")
th1 = threading.Thread(target=task1)
th2 = threading.Thread(target=task2)
th3 = threading.Thread(target=task3)
th4 = threading.Thread(target=task4)
th1.start()
th1.join()
th2.start()
th2.join()
th3.start()
th3.join()
th4.start()
th4.join()

time.sleep(2)  # for thread finished
"""
result is:

First answer
하나
둘
셋
야

but this way it not recommended and there is no profit using thread !
moreover multithreading approach has some overhead for managing threads and lock
it means you waste your resource
"""

# Second answer
# Using index

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

print("Second answer")
thread = []
all_result = []
with ThreadPoolExecutor(max_workers=4) as executor:
    thread.append((1, executor.submit(task1)))
    thread.append((2, executor.submit(task2)))
    thread.append((3, executor.submit(task3)))
    thread.append((4, executor.submit(task4)))

    for idx, task in thread:
        result = task.result()
        all_result.append((idx, result))

all_result.sort(key=lambda x: x[0])
for x in all_result:
    print(x[1])

"""
result is :

하나
둘
셋
야

"""
# If you want one function and return in order

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def task(num):
    return num ** 2


with ThreadPoolExecutor(max_workers=4) as executor:
    future_lst = [executor.submit(task, num) for num in nums]
    for future in future_lst:
        print(future.result())

"""
reuslt is :
1
4
9
16
25
36
49
64
81
100

but when use as_complete it is unpredictable 
"""
with ThreadPoolExecutor(max_workers=4) as executor:
    future_lst = [executor.submit(task, num) for num in nums]
    for future in concurrent.futures.as_completed(future_lst):
        print(future.result())
"""
result is:
9
81
25
36
64
16
4
1
100
49
"""
# if you want iterable object and order "map" is good choice
with ThreadPoolExecutor(max_workers=4) as executor:
    future_lst = executor.map(task, nums)
    for future in future_lst:
        print(future)
"""
result is:
1
4
9
16
25
36
49
64
81
100

map is similar to map(func, *iterables) except:
but the iterables are collected immediately rather than lazily and 
func is executed asynchronously and several calls to func may be made concurrently.

map - official docs

When using ProcessPoolExecutor, this method chops iterables into a number of chunks which it submits to the pool as separate tasks. 
The (approximate) size of these chunks can be specified by setting chunksize to a positive integer. 
For very long iterables, using a large value for chunksize can significantly improve performance compared to the default size of 1.
With ThreadPoolExecutor, chunksize has no effect.

https://docs.python.org/3/library/concurrent.futures.html
"""

# Reference
# https://stackoverflow.com/questions/67189283/how-to-keep-the-original-order-of-input-when-using-threadpoolexecutor
# Or using concurrent.futures.threadpoolexecutor and map method, you can run thread iterable.
# And also result return iterable object
