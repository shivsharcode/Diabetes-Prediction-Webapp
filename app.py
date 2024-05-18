
from flask import Flask, render_template, redirect, url_for, request
from Diabetes_python import diabetes_predictor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', form_data=None, result=None)

@app.route('/submit', methods=['POST', 'GET'])
def data_entry():
    form_data = {}
    if request.method == 'POST':
        form_data = {
            'pregnancies': [int(request.form['pregnancies'])],
            'glucose': [int(request.form['glucose'])],
            'diastolic': [int(request.form['diastolic'])],
            'triceps': [int(request.form['triceps'])],
            'insulin': [int(request.form['insulin'])],
            'bmi': [float(request.form['bmi'])],
            'dpf': [float(request.form['dpf'])],
            'age': [int(request.form['age'])]
        }
        
        result = diabetes_predictor(form_data)
        return render_template('index.html', form_data=form_data, result=result)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
