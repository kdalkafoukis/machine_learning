# [Tensorflow](https://www.tensorflow.org/)

### virtual environment

- https://docs.python-guide.org/dev/virtualenvs/

### virtual env

- `pip install virtualenv`

- in the project folder run `virtualenv venv`
- `source venv/bin/activate`
- `deactivate`
- `pip freeze > requirements.txt`
- create the file requirements.txt after installing the right dependencies `pip install -r requirements.txt`

### venv

- https://docs.python.org/3/library/venv.html
- `python3 -m venv venv`

### ffmpeg

- https://superuser.com/questions/746969/ffmpeg-to-convert-from-flac-to-wav

### matplotlib

- https://matplotlib.org/3.1.0/faq/osx_framework.html

### XOR keras resources

- https://gist.github.com/cburgdorf/e2fb46e5ad61ed7b9a29029c5cc30134

- https://blog.thoughtram.io/machine-learning/2016/11/02/understanding-XOR-with-keras-and-tensorlow.html

### implementation

- simplest xor implementation with 2 hidden layers and one output

### train the model

- run `python train_xor_model.py`

trains the model and saves it along with the weights on disk

### run the model

run `python run_xor_model.py`

loads the model and weight from disk and makes predictions
for XOR truth table

### Flask input

eg. http://127.0.0.1:5000/1,0
