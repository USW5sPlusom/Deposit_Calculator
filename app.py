from flask import Flask, render_template, request, url_for
from calculator import Calc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = float(request.form['start'])
        rate = float(request.form['rate'])
        years = int(request.form['years'])
        monthly_deposit = float(request.form.get('monthly_deposit', 0))

        c = Calc(start, rate, years, monthly_deposit)
        end, profit, history = c.calc()

        return render_template('index1.html', end=end, profit=profit)
    return render_template('index1.html')
@app.route('/next_page')
def next_page():
    return render_template('index2.html')

