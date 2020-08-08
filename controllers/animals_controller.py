from flask import Blueprint, render_template, redirect
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route('/animals')
def index():
    animals = animal_repository.select_all()
    return render_template('/animals/index.html', animals=animals, title='All Animals')

@animals_blueprint.route('/animals/<id>')
def show(id):
    animal = animal_repository.select(id)
    return render_template('/animals/show.html', animal=animal, title=animal.name)

@animals_blueprint.route('/animals/<id>/delete')
def delete(id):
    animal_repository.delete(id)
    return redirect('/animals')

@animals_blueprint.route('/animals/new')
def get_info_for_new():
    vets = vet_repository.select_all()
    return render_template('/animals/new.html', vets=vets, title='New Animal')

@animals_blueprint.route('/animals', methods=['POST'])
def create_new_animal():
    pass

@animals_blueprint.route('/animals/<id>/edit')
def get_info_for_update(id):
    pass

@animals_blueprint.route('/animals/<id>', methods=['POST'])
def update_animal(id):
    pass