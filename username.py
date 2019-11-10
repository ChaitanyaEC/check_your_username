from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_username():
	return render_template('index_username.html')

@app.route('/report_username')
def report_username():

	lower_letter = False
	upper_letter = False
	num_end = False

	username = request.args.get('username')

	lower_letter = any(letter.islower() for letter in username)
	upper_letter = any(letter.isupper() for letter in username)
	num_end = username[-1].isdigit()

	report_username = lower_letter and upper_letter and num_end

	return render_template('report_username.html', report_username = report_username, 
							lower = lower_letter, upper = upper_letter, num = num_end)

if __name__ == '__main__':
	app.run(debug = True)
