import time
from valkka.core import *

class LiveStream:
    def __init__(self, shmem_buffers, shmem_name, address, slot):
        self.shmem_buffers = shmem_buffers
        self.shmem_name = shmem_name
        self.address = address
        self.slot = slot

        #RBGShmem Filter
        self.shmem_filter = RGBShmemFrameFilter(self.shmem_name, shmem_buffers, 1920, 1080)

        #SWS Filter
        self.sws_filter = SwScaleFrameFilter(f"sws_{self.shmem_name}", 1920, 1080, self.shmem_filter)

        # decoding part
        self.avthread = AVThread("avthread", self.sws_filter)
        self.av_in_filter = self.avthread.getFrameFilter()

        # define connection to camera
        self.ctx =LiveConnectionContext(LiveConnectionType_rtsp, self.address, self.slot, self.av_in_filter)

        self.avthread.startCall()
        self.avthread.decodingOnCall()

    def close(self):
        self.avthread.decodingOffCall()
        self.avthread.stopCall()

def start_valkka(camera_indexes, shmem_names = [], prod=False):
    livestreams = {}

    #Defining livethread
    livethread = LiveThread("livethread")

    # Defining filter
    shmem_filters = {}
    sws_filters = {}
    for i in range(1, len(camera_indexes) + 1):
        livestreams[i] = LiveStream(7, f"CAM_{i}", camera_indexes[i-1], i)

    #Start livethread
    livethread.startCall()

    # Register context to livethread
    for livestream in livestreams.values():
        livethread.registerStreamCall(livestream.ctx)
        livethread.playStreamCall(livestream.ctx)
        shmem_names.append(livestream.shmem_name)

    if prod:
        while True:
            continue
    else:
        time.sleep(36000)
    
    for livestream in livestreams.values():
        livestream.close()
    livethread.stopCall()
    return True
    print("bye")