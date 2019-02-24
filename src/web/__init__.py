from flask import Flask, url_for
import os

UPLOAD_FOLDER = 'web/uploads/'
THE_EXTENSIONS = set(['bed'])

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# Cache busting
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


# noinspection PyUnresolvedReferences
from web import routes
