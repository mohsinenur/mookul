from flask import Blueprint, render_template

mod = Blueprint('comesoon', __name__, template_folder='templates')


@mod.route('/')
def index():
    return render_template('coming-soon.html')
