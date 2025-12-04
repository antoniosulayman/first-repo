import threading
import requests
import time


def fetch(num: int):
    print("Requesting", num, "...")
    requests.get("https://httpbin.org/delay/2")
    print("got response", num)
    
  


start = time.time()

for i in range(10):
    fetch(i)

print(f"saquentially: {time.time() - start:.2f} cek")



#===================================================================#