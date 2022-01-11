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
        #takes name field from form and assigns to query_name
        query_name = request.form['name']
        #lowers query_name string to capture all matches whether or not string is capitalized
        query_name = query_name.lower()
        #reads in patient information dataframe
        df = pd.read_csv('data/patient_tb.csv')
        #lowers PatientFirstName column to match lower string of query name
        df['PatientFirstName']= df['PatientFirstName'].str.lower()
        #filters dataframe for only matches of query_name and 'PatientFirstName' column
        result_df = df[df['PatientFirstName']== query_name]
        #removes duplicates rows if matched on subset columns
        result_df2 = result_df.drop_duplicates(subset=['PatientFirstName', 'PatientLastName', 'TestName', 'MostRecentTestDate'])
        #returns rendered html with sliced dataframe and dropped duplicates
        #if nothing is entered, entire dataframe is returned to see names to search on
        if query_name == '':
            return render_template("search.html", tables = [df.to_html(classes='table-striped table-dark')])
        #returns rendered html with sliced dataframe and dropped duplicates
        else:
            return render_template("search.html", tables = [result_df2.to_html(classes='table-striped table-dark')])
    
    
    
    return render_template("search.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
