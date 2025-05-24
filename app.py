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
        plot_url = c.generate_plot(history)

        return render_template('base.html', end=end, profit=profit, plot_url=plot_url)
    return render_template('base.html')
@app.route('/next_page')
def next_page():
    return render_template('base2.html')

