from flask import Flask, render_template

from flask import render_template,flash,redirect




app = Flask(__name__,template_folder="template")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ambassodor')
def Ambassodor():
    return render_template('Ambassodor.html')

@app.route('/Programs')
def Programs():
    return render_template('Programs.html')

# if __name__ == '__main__':
app.run(debug=True)