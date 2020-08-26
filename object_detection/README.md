# NLP for greek language

### virtual environment

- https://docs.python-guide.org/dev/virtualenvs/

### virtual env

- `pip install virtualenv`

- in the project folder run `virtualenv venv`
- `source venv/bin/activate`
- `deactivate`
- `pip freeze > requirements.txt`
- create the file requirements.txt after installing the right dependencies `pip install -r requirements.txt`

### yolo

- https://pjreddie.com/darknet/yolo/

```
git clone https://github.com/pjreddie/darknet
cd darknet
make
```

### run

- `python video_object_detection2.py --video videos/test_video.mp4 --weights darknet/yolov3.weights --configs darknet/cfg/yolov3.cfg --class_names darknet/data/coco.names`

- `python video_object_detection.py`