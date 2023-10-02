from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, DecimalField
from wtforms.validators import DataRequired


class SymbolSelectionForm(FlaskForm):
    chart_select = SelectField(u'Select symbol:', choices = [
                                        ('qqq', 'QQQ'),
                                        ('exp1', 'Example 1'),
                                        ('mmo2', 'MMO2'),
                                        ('spy', 'SPY')
                                        ]
                                )

    scale_select = SelectField('Scale Type:', choices = [
                                        ('linear', 'Linear'),
                                        # ('Logarithmic', 'log'),
                                        ('variable', 'Variable')
                                        ]
                                )

    submit = SubmitField('Submit')

class ParamSelectionForm(FlaskForm):
    reversal = SelectField(u'Reversal Size:', choices = list(range(2, 6)))
    # box_size = DecimalField('Box Size')
    # plot_select = RadioField('Plot Method: ', choices = [
    #                                         ('High-Low', 'high-low'),
    #                                         ('Close / Last', 'close')
    #                                         ]
    #                         )

    submit = SubmitField('Generate Chart')

'''
Add to line 44 of the home template:

                <div class="input-group mb-3">
                    {{ form2.box_size.label(class_="input-group-text") }}
                    {{ form2.box_size(class_="form-control") }}
                </div>
                Scale Method
                {% for subfield in form2.scale_select %}
                    <div class="form-check">
                        {{ subfield(class_="form-check-input") }}
                        {{ subfield.label(class_="form-check-label")}}
                    </div>
                {% endfor %}
'''
