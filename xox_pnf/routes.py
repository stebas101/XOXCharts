from flask import render_template, url_for, redirect, request, session
from . import app
from .pnfplot import PnfChart
from .forms import SymbolSelectionForm, ParamSelectionForm

# Hardcoded parameters for testing:
from .harcoded_parameters import *
# chart_data = [
#     [1, [36,37, 38, 39, 40]],
#     [-1, [37, 38, 39]],
#     [1, [38, 39, 40]]
#     ]


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form  = SymbolSelectionForm()
    form2 = ParamSelectionForm()

    if form.validate_on_submit() and form.submit.data:
        selection = form.chart_select.data
        session['selection'] = selection
        session['chart_params'] = None

        # return redirect(url_for('home'))

        return render_template('home.html', title="XOX - Point-And-Figure",
                            selection = selection,
                            form = form,
                            form2 = form2
                            )

    if form2.validate_on_submit() and form2.submit.data:
        selection = session.get('selection')
        chart_params = file_dict.get(selection)
        chart_params['reversal_size'] = int(form2.reversal.data)
        pnf_chart = PnfChart(chart_params)
        day1 = pnf_chart.first_day
        day2 = pnf_chart.last_day
        day1_str = f'{day1.day_name()}, {day1.day} {day1.month_name()} {day1.year}'
        day2_str = f'{day2.day_name()}, {day2.day} {day2.month_name()} {day2.year}'
        session['chart_params'] = chart_params
        session['date_range'] = [day1_str, day2_str]
        session['chart'] = pnf_chart.text

        return render_template('home.html', title="XOX - Point-And-Figure",
                            selection = selection,
                            chart_params = session['chart_params'],
                            date_range = session['date_range'],
                            chart = session['chart'],
                            # chart_data = chart_data,
                            # chart_scale = chart_scale,
                            form = form,
                            form2 = form2
                            )

    # else:
    session['selection'] = None
    session['chart_params'] = None

    return render_template('home.html', title="XOX - Point-And-Figure",
                            selection = session.get('selection'),
                            chart_params = session.get('chart_params'),
                            date_range = session.get('date_range'),
                            chart = session.get('chart'),
                            form = form,
                            form2 = form2
                            )

@app.route("/about")
def about():
    return render_template('about.html', title="XOX-PnF - About")
