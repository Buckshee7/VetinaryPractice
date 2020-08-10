from flask import Flask, render_template
import datetime
import repositories.treatment_repository as treatment_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

app = Flask(__name__)

#import blueprints
from controllers.vets_controller import vets_blueprint
from controllers.animals_controller import animals_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.treatments_controller import treatments_blueprint

#register blueprints
app.register_blueprint(vets_blueprint)
app.register_blueprint(animals_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(treatments_blueprint)

@app.route('/')
def home():
    owners = owner_repository.select_all()
    animals = animal_repository.select_all()
    vets = vet_repository.select_all()
    counts = {'owners':len(owners), 'animals':len(animals), 'vets':len(vets)}
    date_today = datetime.datetime.now().date()
    treatments = treatment_repository.select_all()
    treatments_today = [treatment for treatment in treatments if treatment.date == date_today]
    return render_template('index.html', treatments_today=treatments_today, counts=counts, title='Home')

if __name__ == '__main__':
    app.run(debug=True)