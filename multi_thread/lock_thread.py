import concurrent.futures
import threading
import time

global_v = 0
thread_lock = threading.Lock()

'''
Multi-Threading with Lock vs sequential code 
there isn't much difference except that the multithreading approach has some overhead for managing threads and lock.
'''

def thread_test(num, index):
    thread_lock.acquire()
    global global_v
    for _ in range(num):
        global_v += 1
    print(f"thread_{index} end")
    print(f"global_v is {global_v}")
    thread_lock.release()


# make thread fool
thread_1 = threading.Thread(target=thread_test, args=(3000000, 1))
thread_2 = threading.Thread(target=thread_test, args=(3000000, 2))
thread_3 = threading.Thread(target=thread_test, args=(3000000, 3))
thread_4 = threading.Thread(target=thread_test, args=(3000000, 4))
thread_5 = threading.Thread(target=thread_test, args=(3000000, 5))

thread_start = time.perf_counter()
# start thread
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_end = time.perf_counter()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
print(f"multithread run takes {thread_end-thread_start:.5f} sec")
'''
threading result is 

thread_1 end
global_v is 1000000
thread_2 end
global_v is 2000000
thread_3 end
global_v is 3000000
thread_4 end
global_v is 4000000
thread_5 end
global_v is 5000000

gloval_v and thread order is perfect.

Q. what is the different point between multithread using lock and just for loop running? 
my stack over flow Question.
https://stackoverflow.com/questions/75508198/python-multithreading-is-faster-than-sequential-code-why
https://stackoverflow.com/questions/75516141/python-multi-threading-with-lock-is-much-faster-why
'''

def increment():
    global nomal_result

    for _ in range(15_000_000):
        nomal_result += 1


nomal_result = 0

start_time = time.perf_counter()
increment()
end_time = time.perf_counter()

print(f"nomal run takes {end_time-start_time:.5f} sec")

"""
 multithread run takes 0.17208 sec
 but nomal run takes 0.38800 sec
"""
