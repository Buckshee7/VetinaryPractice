from flask import Flask, render_template

app = Flask(__name__)

#import blueprints
from controllers.vets_controller import vets_blueprint
from controllers.animals_controller import animals_blueprint

#register blueprints
app.register_blueprint(vets_blueprint)
app.register_blueprint(animals_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)