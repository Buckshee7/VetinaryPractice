from flask import Blueprint, render_template, redirect, request
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
from models.owner import Owner

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route('/owners')
def index():
    owners = owner_repository.select_all()
    return render_template('/owners/index.html', owners=owners, title='Owners')

@owners_blueprint.route('/owners/<id>')
def show(id):
    owner = owner_repository.select(id)
    animals = owner_repository.animals(owner)
    return render_template('/owners/show.html', owner=owner, animals=animals, title=f"{owner.title} {owner.last_name}")

@owners_blueprint.route('/owners/<id>/delete')
def delete(id):
    owner = owner_repository.select(id)
    animals = owner_repository.animals(owner)
    for animal in animals:
        animal_repository.delete(animal.id)
    owner_repository.delete(id)
    return redirect('/owners')

@owners_blueprint.route('/owners/new')
def get_info_for_new():
    return render_template('/owners/new.html', title='New Owner')

@owners_blueprint.route('/owners', methods=['POST'])
def create_new_owner():
    title = request.form['title']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    registered = True if request.form['registered'] == "True" else False
    new_owner = Owner(title, first_name, last_name, phone, registered)
    owner_repository.save(new_owner)
    return redirect('/owners')

@owners_blueprint.route('/owners/<id>/edit')
def get_info_for_update(id):
    owner = owner_repository.select(id)
    return render_template('/owners/edit.html', owner=owner, title=f'Update {owner.title} {owner.last_name}')

@owners_blueprint.route('/owners/<id>', methods=['POST'])
def update_owner(id):
    title = request.form['title']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    registered = True if request.form['registered'] == "True" else False
    updated_owner = Owner(title, first_name, last_name, phone, registered, id)
    owner_repository.update(updated_owner)
    return redirect('/owners')