from flask import render_template
import json
from web import backend

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


    return render_template('index.html')

def about():
    return render_template('about.html')