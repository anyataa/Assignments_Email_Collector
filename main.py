# landing page: Control how the UI look like alongside with each features functionality 
from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    # Showing the .csv file
    with open('./csv.csv') as file:
        reader = csv.reader(file)
        return render_template('landing_page.html', csv=reader)

if __name__ == '__main__':
    app.run(debug=True)
