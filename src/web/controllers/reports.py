from flask import render_template
from web import backend
from web import graphs


def view_report():
    data = backend.lines[0]

    graphs.generate_chromosome_images(data)


    return render_template('displayreport.html', img_name="testingplot.png")
