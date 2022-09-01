from logging import PlaceHolder
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators, DateField, TimeField, FileField, FieldList, FormField, RadioField, IntegerField, SubmitField, SelectMultipleField
from wtforms.fields import EmailField, DateField

class carbonForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    birthdate = DateField('Date of Birth', [validators.length(max=8), validators.Optional()])
    password = PasswordField('Password', [validators.Length(min=8, max=20), validators.DataRequired()])
    comfirmpw = PasswordField('Confirm Password', [validators.Length(min=8, max=20), validators.DataRequired()])


class carbonfootprint(Form):
    numberofpeople = IntegerField('Number of people in your household: ', [validators.DataRequired(), validators.NumberRange(min=1, max=10)])
    electricity = IntegerField('Electricity Consumption for the past month in $', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    gas = IntegerField('Gas Consumption for the past month in $', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    water = IntegerField('Water Consumption for the past month in $', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    recycle = SelectField('Does your household recycle waste?', [validators.DataRequired()],choices=[('', 'Select'), ('1', 'Yes'), ('0', 'No')], default="Select")
    car = IntegerField('Car (in km)', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    motorcycle = IntegerField('Motorcycle (in km)', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    mrtlrt = IntegerField('MRT/LRT (in km)', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    bus = IntegerField('Bus (in km)', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    southeastasia = IntegerField('Southeast Asia: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    asiapacific = IntegerField('Asia Pacific', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    europeafrica = IntegerField('Europe/Africa: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    oceania = IntegerField('Oceania (Australia): ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    americas = IntegerField('North America/South America: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    food = SelectField('Which of the following best describes your diet?', [validators.DataRequired()], choices=[('', 'Select'), (83.33, 'Vegan'), (125,'Vegetarian'), (166.67,'No Beef (Meat intake consists of chicken, fish and pork)'), (208.33,'Average'), (250,'Meat Lover')], default="Select")
    medical = IntegerField('Medical Fees: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    insurance = IntegerField('Insurance: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    education = IntegerField('Education: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    goodsandservices = IntegerField('Goods and Services: ', [validators.DataRequired(), validators.NumberRange(min=0)], default='0')
    email = StringField('Email:', [validators.DataRequired()])

