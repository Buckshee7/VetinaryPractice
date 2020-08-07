from flask import Flask, render_template

app = Flask(__name__)

#import blueprints
#register blueprints

@app.route('/')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)