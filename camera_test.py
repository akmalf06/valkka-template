import threading
import time
import json

from server import start_valkka
from client import show_frame

config = {}
# Load config
with open("./config.json", "r") as f:
    config = json.load(f)

camera_indexes = config.get("target_camera_indexes", [0])

shmem_names = []  
client_threads = []

if __name__ == '__main__':
    #Start server thread
    print("Starting Camera...")
    server_thread = threading.Thread(target=start_valkka, args=(camera_indexes, shmem_names, False))
    server_thread.start()
    time.sleep(3)
    print(f"Total shmem: {len(shmem_names)}")

    #Start client thread
    for shmem_name in shmem_names:
        thread = threading.Thread(target=show_frame, args=(shmem_name, 7))
        client_threads.append(thread)
        thread.start()

    time.sleep(60)

    server_thread.join()
    for thread in client_threads:
        thread.join()