from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class ChartSelectionForm(FlaskForm):
    chart_select = SelectField(u'Select chart: ', choices = [
                                        ('qqq', 'QQQ'),
                                        ('exp1', 'Example 1'),
                                        ('mmo2', 'MMO2')
                                        ]
                                    )
    submit = SubmitField('Get Chart')