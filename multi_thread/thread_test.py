"""
Why does join function need?

Check the parent thread end time and child thread end time.

"join" makes parent thread wait until child thread finished
"""

import threading

global_v = 0


def thread_test(num, index):
    global global_v
    for _ in range(num):
        global_v += 1
    print(f"thread_{index} end")
    print(global_v)


# make thread fool
thread_1 = threading.Thread(target=thread_test, args=(1000000, 1))
thread_2 = threading.Thread(target=thread_test, args=(1000000, 2))
thread_3 = threading.Thread(target=thread_test, args=(1000000, 3))
thread_4 = threading.Thread(target=thread_test, args=(1000000, 4))
thread_5 = threading.Thread(target=thread_test, args=(1000000, 5))

# start thread
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

print("parent thread end!!")

'''
threading result is 

thread_1 end
1000000
thread_2 end
1631150
thread_3 end
2631150
thread_4 endparent thread end!!

3591666
thread_5 end
4085071

parent thread ended while child thread was running
'''

"""
multi threading with join

join - this function wait until child threads finish

"""
import threading

global_join_v = 0


def thread_test(num, index):
    global global_join_v
    for _ in range(num):
        global_join_v += 1
    print(f"thread_{index} end")
    print(f"global_v is {global_join_v}")


# make thread fool
thread_1 = threading.Thread(target=thread_test, args=(1000000, 1))
thread_2 = threading.Thread(target=thread_test, args=(1000000, 2))
thread_3 = threading.Thread(target=thread_test, args=(1000000, 3))
thread_4 = threading.Thread(target=thread_test, args=(1000000, 4))
thread_5 = threading.Thread(target=thread_test, args=(1000000, 5))

# start thread
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

# "join" function get the parent thread wait until child threads done.
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()

print("parent thread end !!")

'''
threading result is 

thread_1 end
global_join_v is 1000000
thread_2 end
global_join_v is 1506221
thread_3 end
global_join_v is 2469794
thread_4 end
global_join_v is 3124905
thread_5 end
global_join_v is 3469794
parent thread end !!

of course this result not stable. 
it can be changed every running.

because of "join" function 
parent thread ended after child threads had ended

but global_v is still not correct. 
'''
