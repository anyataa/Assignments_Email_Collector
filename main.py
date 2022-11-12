# landing page: Control how the UI look like alongside with each features functionality 
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    upload_file = "Upload file here"
    return render_template('landing_page.html', upload_file= upload_file)

if __name__ == '__main__':
    app.run(debug=True)
