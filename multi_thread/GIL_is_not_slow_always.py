import threading
import time

lock = threading.Lock()
def thread_test():
    time.sleep(1.0)
# thread code
thread_start = time.perf_counter()

thread_1 = threading.Thread(target=thread_test)
thread_2 = threading.Thread(target=thread_test)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

thread_end = time.perf_counter()

print(f"Task duration: {thread_end - thread_start:.5f} sec")

# sequential code
thread_start = time.perf_counter()
thread_test()
thread_test()
thread_end = time.perf_counter()

print(f"Task duration: {thread_end - thread_start:.5f} sec")

"""
result is:
Task duration: 1.01324 sec
Task duration: 2.01808 sec

"""