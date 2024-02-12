import cv2
from valkka.api2 import ShmemRGBClient
import imutils

def show_frame(shmem_name, shmem_buffers):
    client = ShmemRGBClient(
        name=shmem_name,
        n_ringbuffer=shmem_buffers,
        width=1920,
        height=1080,
        mstimeout=1000,
        verbose=False
    )

    while True:
        index, meta = client.pullFrame()
        if (index == None):
            print("timeout")
            continue
        data = client.shmem_list[index][0:meta.size]
        img = data.reshape((meta.height, meta.width, 3))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = imutils.resize(img, 640, 360)
        cv2.imshow(f"VALKKA_VIDEO_{shmem_name}", img)
        cv2.waitKey(1)