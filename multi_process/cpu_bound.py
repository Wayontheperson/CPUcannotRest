from concurrent.futures import ProcessPoolExecutor
import time


COUNTING = 1_000_000
TIMES = 3

def task(num):
    process_cnt = 0
    for _ in range(num):
        process_cnt += 1
    return process_cnt


if __name__ == '__main__':
    test_lst = [COUNTING for _ in range(TIMES)]
    with ProcessPoolExecutor(8) as executor:

        start = time.perf_counter()
        results = executor.map(task, test_lst)
    print("multi run")
    print(f"total time is {time.perf_counter()-start} total value is {sum(results)}")

    start = time.perf_counter()
    cnt = 0
    for i in range(COUNTING*TIMES):
        cnt += 1
    print("\n")
    print("sequential run")
    print(f"total time is {time.perf_counter()-start} total value is {cnt}")

'''
reuslt is:

multi run
total time is 0.6343487999999999 total value is 100_000_000


sequential run
total time is 6.0091941 total value is 100_000_000

But,

when count only 3000000 sequential is fast 

multi run
total time is 0.22341280000000002 total value is 3000000

sequential run
total time is 0.1800659 total value is 3000000
'''