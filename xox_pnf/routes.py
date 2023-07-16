import pandas as pd
from flask import render_template, url_for, redirect, request
from xox_pnf import app
from xox_pnf.pnfplot import get_chart, get_price_data, pnf_text
from xox_pnf.forms import ChartSelectionForm

# Hardcoded parameters for testing:
from xox_pnf.test_parameters import * 


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ChartSelectionForm()

    if form.validate_on_submit():
        selection = form.chart_select.data
        chart_params = file_dict[selection]
        price_data = get_price_data(chart_params['data_file'])
        day1 = price_data.index[0]
        day2 = price_data.index[-1]
        day1_str = f'{day1.day_name()}, {day1.day} {day1.month_name()} {day1.year}'
        day2_str = f'{day2.day_name()}, {day2.day} {day2.month_name()} {day2.year}'
        scale, columns = get_chart(chart_params)
        chart = pnf_text(scale, columns)
        chart = chart.split('\n')
        return render_template('home.html', title="XOX - Point-And-Figure",
                            chart_params = chart_params,
                            date_range = [day1_str, day2_str],
                            chart = chart,
                            form = form
                            )

    return render_template('home.html', title="XOX - Point-And-Figure",
                            chart_params = {},
                            form = form
                            )

@app.route("/about")
def about():
    return render_template('about.html', title="XOX-PnF - About")
