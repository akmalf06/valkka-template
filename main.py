import threading
import time
import json

from server import start_valkka

config = {}
# Load config
with open("./config.json", "r") as f:
    config = json.load(f)

camera_indexes = config.get("target_camera_indexes", [0])

shmem_names = []

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_valkka, args=(camera_indexes, shmem_names, False))
    is_finished = server_thread.start()
    if is_finished:
        server_thread.join()