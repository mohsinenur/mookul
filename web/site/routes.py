from flask import Blueprint, render_template

mod = Blueprint('site', __name__, template_folder='templates')


@mod.route('/')
def home():
	return render_template('home/index.html')


@mod.route('/shop')
def shop():
	return render_template('shop/index.html')


@mod.route('/<shopname>', methods=['GET'])
def singleshop(shopname):
	meter1 = 'bkutir'
	if shopname == meter1:
		return render_template("shop/index.html", para1=meter1)
	else:
		return not_found_error(error=404)


@mod.route('/<username>', methods=['GET'])
def orders(username):
	meter1 = 'mohsin'
	if username == meter1:
		return render_template("/user/orders.html", para1=meter1)
	else:
		return not_found_error(error=404)


@mod.route('/<username>/profile', methods=['GET'])
def profile(username):
	meter1 = 'mohsin'
	if username == meter1:
		return render_template("/user/profile.html", para1=meter1)
	else:
		return not_found_error(error=404)


@mod.route('/<username>/address', methods=['GET'])
def address(username):
	meter1 = 'mohsin'
	if username == meter1:
		return render_template("/user/address.html", para1=meter1)
	else:
		return not_found_error(error=404)


@mod.route('/<username>/wishlist', methods=['GET'])
def wishlist(username):
	meter1 = 'mohsin'
	if username == meter1:
		return render_template("/user/wishlist.html", para1=meter1)
	else:
		return not_found_error(error=404)


# error handle
@mod.errorhandler(404)
def not_found_error(error):
	return render_template('/error/404.html'), 404
