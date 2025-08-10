import threading
import os
import json
from concurrent.futures import ThreadPoolExecutor



def process():
    print("==进程==")


if __name__ == "main":

    files = ["test.json", "test2.json"]
    with ThreadPoolExecutor(max_workers=10) as e:
        futures = [e.submit(process) for file in files]

    for future in futures:
        futures.result()
    
