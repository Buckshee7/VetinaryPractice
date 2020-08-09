from flask import Blueprint, render_template, redirect, request
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import datetime

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
    owners = owner_repository.select_all()
    return render_template('/animals/new.html', vets=vets, owners=owners, title='New Animal')

@animals_blueprint.route('/animals', methods=['POST'])
def create_new_animal():
    name = request.form['name']
    animal_type = request.form['animal_type']
    dob_string = request.form['dob']
    dob = datetime.datetime.strptime(dob_string, '%Y-%m-%d').date()
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    img_url = request.form['img_url'] if request.form['img_url'] else "static/images/no_img.jpg"
    vet_id = None if request.form['vet_id'] == "None" else request.form['vet_id']
    vet = vet_repository.select(vet_id)
    new_animal = Animal(name, dob, animal_type, owner, vet, img_url)
    animal_repository.save(new_animal)
    return redirect('/animals')
    

@animals_blueprint.route('/animals/<id>/edit')
def get_info_for_update(id):
    animal = animal_repository.select(id)
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('/animals/edit.html', animal=animal, vets=vets, owners=owners, title=f"Update {animal.name}")

@animals_blueprint.route('/animals/<id>', methods=['POST'])
def update_animal(id):
    name = request.form['name']
    animal_type = request.form['animal_type']
    dob_string = request.form['dob']
    dob = datetime.datetime.strptime(dob_string, '%Y-%m-%d').date()
    owner_name = request.form['owner_name']
    owner_phone = request.form['owner_phone']
    img_url = request.form['img_url'] if request.form['img_url'] else "static/images/no_img.jpg"
    vet_id = None if request.form['vet_id'] == "None" else request.form['vet_id']
    vet = vet_repository.select(vet_id)
    treatment_notes = "" #to be implemented later
    updated_animal = Animal(name, dob, animal_type, owner_name, owner_phone, vet, img_url, treatment_notes, id)
    animal_repository.update(updated_animal)
    return redirect('/animals')