# Valkka Template
Handling IP Camera connection with AI Inference can be though. Moreover, if the AI must be connected to multiple IP camera, it will produce a lot of delay and consume a lot of computing cost.
Let me introduce valkka as a hero to handle that kind of pain.
## About valkka
Valkka is a python media streaming framework. Mostly, valkka is used to connect IP Camera with the python process, so that module like OpenCV, YOLO, etc. able to consume the frame streamed by the IP Camera. 
Valkka is used because its ability to stream IP Camera media in a real-time with low computing cost. Valkka already tested able to run 14 IP Camera concurrently in my project with IP Camera setting's as like this:
1. Resolution: 1920*1080
2. FPS: 25 FPS

With the current valkka, you should make sure that IP Camera is using h.264 codecs and an edge PC that using Ubuntu OS in order to make valkka run.
## Requirements
In order to use valkka, you need to install this requirements.
1. Ubuntu OS 22.04
2. [Valkka](https://valkka.readthedocs.io/en/latest/)
3. [OpenCV Python](https://pypi.org/project/opencv-python/)
4. [imutils](https://pypi.org/project/imutils/)

## Environtment Variables and Configuration
There is only one configuration file that should be set up: ```config.json```. 
In ```config.json```, there is an object with key ```target_camera_indexes``` as an array. In order to stream all of your IP Camera, you should include your IP Camera's RTSP url in that array.
```json
{
  "target_camera_indexes": [
    "rtsp://user:password@192.168.1.3:554/Streaming/Channels/101/"
  ]
}
```

## Run Valkka
After you set up the requirements and ```config.json```, you are able to test valkka directly using this command.
```python3
python3 camera_test.py
```
After that, you should be able to see multiple window appear that show media streamed by your IP Camera.

## FAQ
#### Q: Why does the window just showing blank black screen when i try to connect valkka to more than 1 camera?
A: You should check opencv version that you are using is same as valkka is using.

## Support
For support contact akmaldavinci06@gmail.com
