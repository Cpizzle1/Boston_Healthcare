from flask import Flask, render_template, request, url_for, flash, redirect
import pandas as pd
from flask.views import View
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrets123'

@app.route('/')
def home():    
    return render_template("home.html")

@app.route('/search', methods=['GET', 'POST']) # if no method is stated, defaults to GET
def search():

    if request.method == 'POST':
        query_name = request.form['name']
        query_name = query_name.lower()
        df = pd.read_csv('data/patient_tb.csv')
        df['PatientFirstName']= df['PatientFirstName'].str.lower()
        result_df = df[df['PatientFirstName']== query_name]
        result_df2 = result_df.drop_duplicates(subset=['PatientFirstName', 'PatientLastName', 'TestName', 'MostRecentTestDate'])

        if not result_df2.empty:
            return render_template("search.html", tables = [result_df2.to_html(classes='table-striped table-dark')])
        else: 
            return render_template("search.html", tables = [df.to_html(classes='table-striped table-dark')])
    
    
    
    return render_template("search.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
