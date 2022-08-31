import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from werkzeug.utils import secure_filename

from form import carbonForm, carbonfootprint
import shelve, user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOAD_FOLDER'] = 'static/images'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/tabs', methods=['GET', 'POST'])
def tabs():
   carbonFootprint = carbonfootprint(request.form)
   if request.method == 'POST':
      users_dict = {}
      db = shelve.open('storage.db', 'c')
      try:
         users_dict = db['Users']
      except:
         print("Error in retrieving Users from storage.db.")

      session['useremail'] = carbonFootprint.email.data

      #   if key == 'None': 
      #       flash('Email does not have records', 'danger')

      peoplecount = carbonFootprint.numberofpeople.data

      # utilities
      if carbonFootprint.electricity.data != 'None':
         electricity = carbonFootprint.electricity.data / 0.3228 * 0.4080
      if carbonFootprint.gas.data > 0:
         gas = carbonFootprint.gas.data / 0.2471 * 0.4080
      if carbonFootprint.water.data > 0:
         water = carbonFootprint.water.data / 0.0129 * 0.137
      utility = electricity + gas + water
      
      if utility < 2:
         utility = 83
      else:
         utility/peoplecount+1

      utility = float(utility)

      # transport
      car = carbonFootprint.car.data * 0.118
      motorcycle = carbonFootprint.motorcycle.data * 0.0227
      mrtlrt = carbonFootprint.mrtlrt.data * 0.0132
      bus = carbonFootprint.bus.data * 0.073

      tranportation = car + motorcycle + mrtlrt + bus
      

      ## regions
      sea = carbonFootprint.southeastasia.data * 256.5
      asia = carbonFootprint.asiapacific.data * 1543.845
      europeafrica = carbonFootprint.europeafrica.data * 2918.115
      oceania = carbonFootprint.oceania.data * 1257.99
      americas = carbonFootprint.americas.data * 2411.385

      tranportation = (tranportation + sea+asia+europeafrica+oceania+americas)/peoplecount
      tranportation = float(tranportation)

      # food
      foods = carbonFootprint.food.data
      foods = float(foods)

      # others
      med = carbonFootprint.medical.data / 0.87
      insurance = carbonFootprint.insurance.data / 211.532
      education = carbonFootprint.education.data / 105.766
      goodsandservices = carbonFootprint.goodsandservices.data / 61.019

      others = (med + insurance + education + goodsandservices)/peoplecount
      otehrs = float(others)

      # total
      total = utility + tranportation + foods + others

      # set values
      usercarbon = user.User(carbonFootprint.email.data, utility, tranportation, foods, others, total)

      users_dict[usercarbon.get_email()] = usercarbon
      db['Users'] = users_dict
      db.close()

      return redirect(url_for('dash', id=carbonFootprint.email.data))
        
   else:
      return render_template('tabform.html', form = carbonFootprint)


@app.route('/carbonform', methods=['GET', 'POST'])
def create_user():
   createform = carbonForm(request.form)

   return render_template('carbonform.html', form = createform)

@app.route('/dashboard/<id>/')
def dash(id):
   users_dict = {}
   db = shelve.open('storage.db', 'r')
   users_dict = db['Users']
   db.close()

   details = users_dict.get(str(id))

   return render_template('dashboard.html')


@app.route('/informativePage')
def informative():
   return render_template('informativePage.html')

if __name__ == '__main__':
    app.run(debug=True)