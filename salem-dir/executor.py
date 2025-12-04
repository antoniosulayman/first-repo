import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def work (seconds):
    pid = __import__('os').getpid()
    print(f"start working {seconds} sec. (process {pid})")
    time.sleep(seconds)
    print(f"Done for {seconds} sec! (process {pid})")

tasks = [3 ,2 ,4 ,1 ,3, 2, 10, 7, 5, 8]

start = time.time()
with ProcessPoolExecutor(max_workers=3) as executor:

    results = executor.map(work, tasks)
    for r in results:
        # print(r)
        ...

print(f"processpoolExecutor time: {time.time() - start:.1f} cek.")

