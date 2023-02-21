import concurrent.futures
import time
import threading
from concurrent.futures import ThreadPoolExecutor


test_lst = [1, 1000000, 2, 3000000]
answer = []


def task(num):
    cnt = 0
    for _ in range(num):
        cnt += 1
    return cnt

# Check time and result when use as_completed.
with ThreadPoolExecutor(max_workers=4) as executor:
    start_thead = time.time()
    future_lst = [executor.submit(task,i) for i in test_lst]
    for future in concurrent.futures.as_completed(future_lst):
        print(future.result())
    end_thread = time.time()
    print(f"{end_thread-start_thead}")
time.sleep(2)
print("next")


# Check time and result without as_completed.
with ThreadPoolExecutor(max_workers=4) as executor:
    start_thead = time.time()
    future_lst = [executor.submit(task, i) for i in test_lst]
    for x in future_lst:
        print(x.result())
    end_thread = time.time()
    print(end_thread-start_thead)

time.sleep(2)
print("next")

# Check time and reuslt of sequential code.
start = time.time()
for i in test_lst:
    task(i)
end = time.time()
print(f"{end-start}")

#https://stackoverflow.com/questions/67189283/how-to-keep-the-original-order-of-input-when-using-threadpoolexecutor