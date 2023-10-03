from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, DecimalField, IntegerField
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
                                        ('log', 'Logarithmic'),
                                        ('variable', 'Variable')
                                        ]
                                )

    submit = SubmitField('Submit')

class ParamSelectionForm(FlaskForm):
    reversal = SelectField(u'Reversal Size:', choices = list(range(2, 6)))
    box_size = DecimalField('Box Size')
    # box_log = IntegerField('% Box')
    # box_var = SelectField('Table:', choices = ['Standard'])

    submit = SubmitField('Generate Chart')

