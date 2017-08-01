# Code Challenge.

## Run app.
```sh
virtualenv myenv
source myenv/bin/activate
cd myenv
git clone git@github.com:rodrigodelmonte/vireal.git
cd app/
pip install -r requirements.txt
FLASK_APP=app.py flask run
```

## Test app.
python run_tests.py