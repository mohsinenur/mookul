from flask import Flask, render_template

from web import site, admin, comesoon

from web.comesoon.routes import mod
from web.site.routes import mod
from web.admin.routes import mod

# coming soon app
cs = Flask(__name__)
cs.register_blueprint(comesoon.routes.mod)

# final app
app = Flask(__name__)
app.register_blueprint(site.routes.mod)
app.register_blueprint(admin.routes.mod, url_prefix='/admin')


# error handle for cs
@cs.errorhandler(404)
def not_found_error(error):
	return render_template('404cs.html'), 404


# error handle for app
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404
