from flask import Blueprint, render_template, redirect, request
import repositories.vet_repository as vet_repository
import datetime
from models.vet import Vet

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def index():
    vets = vet_repository.select_all()
    return render_template('/vets/index.html', vets=vets, title='Vets')

@vets_blueprint.route('/vets/<id>')
def show(id):
    vet = vet_repository.select(id)
    animals = vet_repository.animals(id)
    treatments = vet_repository.treatments(id)
    date_today = datetime.datetime.now()
    treatments_future = [treatment for treatment in treatments if treatment.date >= date_today.date()]
    treatments_past = [treatment for treatment in treatments if treatment.date < date_today.date()]
    return render_template('/vets/show.html', vet=vet, animals=animals, treatments_future=treatments_future, treatments_past=treatments_past, title=f"Dr {vet.last_name}")

@vets_blueprint.route('/vets/<id>/delete')
def delete(id):
    vet_repository.delete(id)
    return redirect('/vets')

@vets_blueprint.route('/vets/new')
def get_info_for_new():
    return render_template('/vets/new.html', title='New Vet')

@vets_blueprint.route('/vets', methods=['POST'])
def create_new_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url'] if request.form['img_url'] else "static/images/no_img.jpg"
    new_vet = Vet(first_name, last_name, img_url)
    vet_repository.save(new_vet)
    return redirect('/vets')

@vets_blueprint.route('/vets/<id>/edit')
def get_info_for_update(id):
    vet = vet_repository.select(id)
    return render_template('/vets/edit.html', vet=vet, title='Update Vet')

@vets_blueprint.route('/vets/<id>', methods=['POST'])
def update_vet(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url'] if request.form['img_url'] else "static/images/no_img.jpg"
    updated_vet = Vet(first_name, last_name, img_url, id)
    vet_repository.update(updated_vet)
    return redirect('/vets')