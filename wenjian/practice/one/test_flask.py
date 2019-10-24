from flask import Flask


app = Flask(__name__)


def upgradetest(app):
	@app.route('/upgrade/', methods=['GET'])
	def upgrade_test():
		return '200'
	return app

if __name__ == '__main__':
	app = upgradetest(app)
	app.run()