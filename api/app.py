from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///readnyc.db'
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), unique=False)
	last_name = db.Column(db.String(80), unique=False)
	email = db.Column(db.String(120), unique=True)
	phone = db.Column(db.String(12), unique=True)
	zipcode = db.Column(db.String(5), unique=False)
	main_library = db.relationship('Library', backref='user', uselist=False)
	libraries = db.relationship('Library', backref='users', lazy='dynamic')

	def __init__(self, phone, zipcode):
		self.phone = phone
		self.zipcode = zipcode

	def __repr__(self):
		return '<User %r>' % self.phone

	def __str__(self):
		return self.phone

class Library(db.Model):
	__tablename__ = 'libraries'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	city = db.Column(db.String(20), unique=False)
	additional_address_information = db.Column(db.String(10), unique=False)
	longitude = db.Column(db.Float, unique=False)
	description = db.Column(db.String(200), unique=False)
	displayed_hours = db.Column(db.String(150), unique=False)
	eligibility_information = db.Column(db.String(5), unique=False)
	brief_description = db.Column(db.String(50), unique=False)
	zipcode = db.Column(db.String(5), unique=False)
	value = db.Column(db.String(200), unique=False)
	label = db.Column(db.String(50), unique=False)
	latitude = db.Column(db.Float, unique=False)
	state = db.Column(db.String(2), unique=False)
	facility_id = db.Column(db.String(60), unique=False)
	expiration = db.Column(db.String(20), unique=False)
	long = db.Column(db.String(20), unique=False)
	address = db.Column(db.String(40), unique=False)
	lat = db.Column(db.String(20), unique=False)
	borough = db.Column(db.String(20), unique=False)
	facility_type = db.Column(db.String(10), unique=False)
	facility_name = db.Column(db.String(75), unique=False)
	#features = db.Column(db.String(30), unique=False)

	def __init__(self, args):
		self.city = args['city']
		self.additional_address_information = args['additional_address_information']
		self.longitude = args['longitude']
		self.description = args['description']
		self.displayed_hours = args['displayed_hours']
		self.eligibility_information = args['eligibility_information']
		self.brief_description = args['brief_description']
		self.zipcode = args['zipcode']
		self.value = args['value']
		self.label = args['label']
		self.latitude = args['latitude']
		self.state = args['state']
		self.facility_id = args['id']
		self.expiration = args['expiration']
		self.long = args['long']
		self.address = args['address']
		self.lat = args['lat']
		self.borough = args['borough']
		self.facility_type = args['type']
		self.facility_name = args['facility_name']

	def __repr__(self):
		return '<Library %r>' % self.facility_name

	def __str__(self):
		return self.facility_name
