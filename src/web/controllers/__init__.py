import os

from flask import render_template, request, flash, redirect
from werkzeug.utils import secure_filename

from web import THE_EXTENSIONS, app, backend

import uuid


def index():
    # data = backend.get_data(0) # 0 is file index
    #
    # formatted_data = {}
    #
    # for key in data:
    #     formatted_data[key] = {
    #         "overlaps": [
    #
    #         ],
    #         "ref_gaps": [
    #
    #         ],
    #         "total": ...
    #     }

    return render_template('index.html', result_json=backend.bed_to_json(backend.lines[2]))


def about():
    return render_template('about.html')


def create_report():
    return render_template('createreport.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ["bed"]


def accept_files():
    num_files = 0
    for k, v in request.files.items():
        if "file-" in v.name:
            num_files += 1
    if num_files < 2:
        flash('You must upload at least 2 files.')
        return redirect("/createreport")

    num_saved = 0
    for file in request.files.values():
        if file.filename and file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4().hex) + '.bed'))

            num_saved += 1

    if num_saved < 2:
        flash('You must upload at least 2 files. Please make sure they end in .BED.')
        return redirect("/createreport")
    else:
        return 'success'
