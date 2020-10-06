# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:22:44 2020

@author: mdghouse
topic:Banking
"""
from flask import Flask, render_template, request
import joblib




app = Flask(__name__)
model = joblib.load('finalized_model1.sav')
@app.route('/')

def Home():
    return render_template('index.html')


@app.route("/predict", methods=["GET","POST"])

def predict():
    
    if request.method == 'POST':
        age = int(request.form['age'])
        balance = float(request.form['balance']) 
        job = request.form['job']
        if (job == 'entrepreneur'):
            entrepreneur=1
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0
        elif (job == 'management'):
            entrepreneur=0
            management=1
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0
        elif (job == 'technician'):
            entrepreneur=0
            management=0
            technician=1
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0
    
        elif (job == 'admin'):
            entrepreneur=0
            management=0
            technician=0
            admin=1
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0            
            
        elif (job == 'services'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=1
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0    
        elif (job == 'employed'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=1
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0
        elif (job == 'blue-collar'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=1
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=0
        elif (job == 'retired'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=1
            unemployed=0
            housemaid=0
            student=0
            unknown=0
        elif (job == 'unemployed'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=1
            housemaid=0
            student=0
            unknown=0
        elif (job == 'housemaid'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=1
            student=0
            unknown=0
        elif (job == 'student'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=1
            unknown=0
        elif (job == 'unknown'):
            entrepreneur=0
            management=0
            technician=0
            admin=0
            services=0
            employed=0
            blue_collar=0
            retired=0
            unemployed=0
            housemaid=0
            student=0
            unknown=1
            
            
            
            
            
                
        education = request.form['education']
        if  (education =='primary'):
            primary=1
            secondary=0
            tertiary=0
            unknown=0
          
        elif (education == 'secondary'):
            primary=0
            secondary=1
            tertiary=0
            unknown=0
            
            
        elif (education == 'tertiary'):
            primary=0
            secondary=0
            tertiary=1
            unknown=0
            
        
            
         
            
        housing = int(request.form['housing'])    
        loan = int(request.form['loan'])
        default = int(request.form['default']) 
        
        prediction=model.predict([[entrepreneur,
            management,
            technician,
            admin,
            services,
            employed,
            blue_collar,
            retired,
            unemployed,
            housemaid,
            student,
            unknown,primary,
            secondary,
            tertiary,housing,loan,age,default ,balance]])
        print(prediction)
    
        if prediction==0:
            return render_template('index.html',prediction_texts="will not take loan")
        else:
            return render_template('index.html',prediction_texts="may take loan")
        
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
	app.run(debug=True)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
       