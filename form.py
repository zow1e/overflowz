from logging import PlaceHolder
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators, DateField, TimeField, FileField, FieldList, FormField, RadioField, IntegerField, SubmitField
from wtforms.fields import EmailField, DateField

class carbonForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    birthdate = DateField('Date of Birth', [validators.length(max=8), validators.Optional()])
    password = PasswordField('Password', [validators.Length(min=8, max=20), validators.DataRequired()])
    comfirmpw = PasswordField('Confirm Password', [validators.Length(min=8, max=20), validators.DataRequired()])


class carbonfootprint(Form):
    numberofpeople = IntegerField('Number of people in your household: ', [validators.DataRequired()])
    electricity = IntegerField('Electricity Consumption in $ (Optional)', [validators.Optional()])
    gas = IntegerField('Gas Consumption in $ (Optional)', [validators.Optional()])
    water = IntegerField('Water Consumption in $ (Optional)', [validators.Optional()])
    recycle = RadioField('Does your household recycle waste?', [validators.DataRequired()],choices=[('', 'Select'), ('1', 'Yes'), ('0', 'No')], default='')

