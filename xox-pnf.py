import pandas as pd
import numpy as np
from flask import Flask, render_template, url_for, redirect, request
from pnfplot import get_chart, pnf_text
from forms import ChartSelectionForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aasdfr3434' # Generate new key using secrets

# Dummy data:
qqq = {
    'data_file': 'QQQ.csv',
    'reversal_size': 3,
    'box_size': 10,
    'plot_method': 'high-low',
    'scale_method': 'linear',
}
exp1 = {
    'data_file': 'EXP1.csv',
    'reversal_size': 3,
    'box_size': 1,
    'plot_method': 'high-low',
    'scale_method': 'linear',
}
mmo2 = {
    'data_file': 'MMO2.csv',
    'reversal_size': 3,
    'box_size': 1,
    'plot_method': 'high-low',
    'scale_method': 'linear',
    }
file_dict = {'qqq': qqq, 'exp1': exp1, 'mmo2': mmo2}


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ChartSelectionForm()

    if form.validate_on_submit():
        selection = form.chart_select.data
        chart_params = file_dict[selection]
        scale, columns = get_chart(chart_params)
        chart = pnf_text(scale, columns)
        chart = chart.split('\n')
        return render_template('home.html', title="XOX - Point-And-Figure",
                            chart_params = chart_params,
                            chart = chart,
                            form = form
                            )

    # chart_params = file_dict['qqq']
    # scale, columns = get_chart(chart_params)
    # chart = pnf_text(scale, columns)
    # chart = chart.split('\n')
    return render_template('home.html', title="XOX - Point-And-Figure",
                            chart_params = {},
                            form = form
                            )

@app.route("/about")
def about():
    return render_template('about.html', title="XOX-PnF - About")


if __name__ == "__main__":
    app.run(debug=True)