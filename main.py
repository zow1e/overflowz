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
      db = shelve.open('storage.db', 'r')
      try:
         users_dict = db['Users']
      except:
         print("Error in retrieving Users from storage.db.")

      #   key = carbonFootprint.email.data
      #   session['useremail'] = key

      #   if key == 'None': 
      #       flash('Email does not have records', 'danger')

      peoplecount = carbonFootprint.numberofpeople.data
      # utilities
      electricity = carbonFootprint.electricity.data / 0.3228 * 0.4080
      gas = carbonFootprint.gas.data / 0.2471 * 0.4080
      water = carbonFootprint.water.data / 0.0129 * 0.137
      utility = electricity + gas + water + 1
      
      if utility < 2:
         utility = 83

      print(utility)

      # transport
      car = carbonFootprint.car.data * 0.118
      motorcycle = carbonFootprint.motorcycle.data * 0.0227
      mrtlrt = carbonFootprint.mrtlrt.data * 0.0132
      bus = carbonFootprint.bus.data * 0.073

      tranportation = car + motorcycle + mrtlrt + bus
      print(tranportation)

      ## regions
      sea = carbonFootprint.southeastasia.data * 256.5
      asia = carbonFootprint.asiapacific.data * 1543.845
      europeafrica = carbonFootprint.europeafrica.data * 2918.115
      oceania = carbonFootprint.oceania.data * 1257.99
      americas = carbonFootprint.americas.data * 2411.385

      tranportation = tranportation + sea+asia+europeafrica+oceania+americas

      return redirect(url_for('dash'))
        
   else:
      return render_template('tabform.html', form = carbonFootprint)



@app.route('/carbonform', methods=['GET', 'POST'])
def create_user():
   createform = carbonForm(request.form)

   return render_template('carbonform.html', form = createform)

@app.route('/dashboard')
def dash():
   return render_template('dashboard.html')

@app.route('/informativePage')
def informative():
   return render_template('informativePage.html')

if __name__ == '__main__':
    app.run(debug=True)