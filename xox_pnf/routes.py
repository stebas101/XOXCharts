from flask import render_template, url_for, redirect, request
from . import app
from .pnfplot import PnfChart
from .forms import ChartSelectionForm

# Hardcoded parameters for testing:
from .harcoded_parameters import * 
# chart_data = [
#     [1, [36,37, 38, 39, 40]],
#     [-1, [37, 38, 39]],
#     [1, [38, 39, 40]]
#     ]

mode = 'text'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ChartSelectionForm()

    if form.validate_on_submit():
        selection = form.chart_select.data
        chart_params = file_dict[selection]
        pnf_chart = PnfChart(chart_params)
        day1 = pnf_chart.first_day
        day2 = pnf_chart.last_day
        day1_str = f'{day1.day_name()}, {day1.day} {day1.month_name()} {day1.year}'
        day2_str = f'{day2.day_name()}, {day2.day} {day2.month_name()} {day2.year}'
        chart = pnf_chart.text
        # chart_scale = list(pnf_chart.scale)

        return render_template('home.html', title="XOX - Point-And-Figure",
                            chart_params = chart_params,
                            date_range = [day1_str, day2_str],
                            chart = chart,
                            mode = mode,
                            # chart_data = chart_data,
                            # chart_scale = chart_scale,
                            form = form
                            )

    return render_template('home.html', title="XOX - Point-And-Figure",
                            chart_params = {},
                            form = form
                            )

@app.route("/about")
def about():
    return render_template('about.html', title="XOX-PnF - About")
