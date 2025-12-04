import requests
import time
import threading

def fetch(num: int):
    print("Requesting", num, "...")
    requests.get("https://httpbin.org/delay/2")
    print("got response", num)

threads = [threading.Thread(target=fetch, args=(i,)) for i in range(10)]

start = time.time()
for t in threads:t.start()
for t in threads:t.join()

print(f"threading: {time.time() - start:.2f}cek")
