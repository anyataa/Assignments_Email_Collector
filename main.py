# landing page: Control how the UI look like alongside with each features functionality 
import csv
import pandas as pd
import os
from flask_cors import CORS
from flask import Flask, redirect, render_template, request, url_for, session, request, abort, send_from_directory
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
# Config for app
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = 'key'
app.config['UPLOAD_EXTENSIONS'] = ['.xls', '.txt', '.csv']
app.config['UPLOAD_PATH'] = 'uploads'




# Create class form to get file input
class InfoForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET'])
def index():

    #  Form
    form = InfoForm()
    # Convert .excel file
    excel_file = pd.read_excel('mock.xls')
    excel_file.to_csv('converted_file_xls.csv',
                        index=None,
                        header=True)
    # Convert .txt file
    text_file = pd.read_csv('mock.txt')
    text_file.to_csv('converted_file_txt.csv',
                            index = None,
                            header = True)
    
    # Showing .csv file
    with open('./converted_file_txt.csv') as file:
        reader = csv.reader(file)
        return render_template('landing_page.html', csv=reader, form = form)

@app.route('/', methods=['POST'])
def upload_file():
    form = InfoForm()
    if form.validate_on_submit():
        session['file'] = form.file.data
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],uploaded_file.filename))
    return redirect(url_for('index'))


@app.route('/uploads/<filename>')
def upload(filename):
    with open(app.config['UPLOAD_PATH']  + '/' + filename) as file:
        reader = csv.reader(file)
        return render_template('show_data.html', csv=reader, filename=filename)

    # Download the report
    # return send_from_directory(app.config['UPLOAD_PATH'], filename)
   

if __name__ == '__main__':
    app.run(debug=True)
