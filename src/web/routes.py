from web import app
from web import controllers
from web.controllers import reports

DEFAULT_DECS = []


def map_route(url, func, **kwargs):
    wrapped_func = func
    if 'decs' in kwargs:
        decs = kwargs.pop('decs')
    else:
        decs = []

    decs += DEFAULT_DECS

    if type(decs) is list:
        for dec in decs:
            wrapped_func = dec(wrapped_func)

    wrapped_func.__name__ = func.__module__ + "." + func.__name__

    app.add_url_rule(url, view_func=wrapped_func, **kwargs)

#######################################################################################
####################                 ROUTES                        ####################
#######################################################################################

map_route('/', controllers.index)
map_route('/about', controllers.about)
map_route('/createreport', controllers.create_report)
map_route('/acceptfiles', controllers.accept_files, methods=["POST"])
map_route('/viewreport', reports.view_report)