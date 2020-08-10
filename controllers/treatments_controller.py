from flask import Blueprint, render_template, request, redirect
import repositories.treatment_repository as treatment_repository
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import datetime
from models.treatment import Treatment

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route('/treatments')
def index():
    treatments = treatment_repository.select_all()
    date_today = datetime.datetime.now()
    treatments_future = [treatment for treatment in treatments if treatment.date >= date_today.date()]
    treatments_past = [treatment for treatment in treatments if treatment.date < date_today.date()]
    return render_template('/treatments/index.html', treatments_future=treatments_future, treatments_past=treatments_past, title='All Treatments')

#do i need this route? I dont really want to have a show page...
# @treatments_blueprint.route('/treatments/<id>')
# def show(id):
#     treatment = treatment_repository.select(id)
#     return render_template('treatments.show.html', treatment=treatment, title='Treatment Details')

#route for delete FROM main treatments page
@treatments_blueprint.route('/treatments/<id>/delete/')
def delete(id):
    treatment_repository.delete(id)
    return redirect('/treatments')

#route for delete FROM vet page
@treatments_blueprint.route('/treatments/<id>/delete/vet')
def delete_from_vet(id):
    treatment = treatment_repository.select(id)
    vet = vet_repository.select(treatment.vet.id)
    treatment_repository.delete(id)
    return redirect(f'/vets/{vet.id}')

#route for delete FROM animal page
@treatments_blueprint.route('/treatments/<id>/delete/animal')
def delete_from_animal(id):
    treatment = treatment_repository.select(id)
    animal = animal_repository.select(treatment.animal.id)
    treatment_repository.delete(id)
    return redirect(f'/animals/{animal.id}')

@treatments_blueprint.route('/treatments/new')
def get_info_for_new():
    return render_template('/treatments/new.html', title='New Treatment')

@treatments_blueprint.route('/treatments', methods=['POST'])
def create_new_vet():
    pass

@treatments_blueprint.route('/treatments/<id>/edit')
def get_info_for_update(id):
    pass

@treatments_blueprint.route('/treatments/<id>', methods=['POST'])
def update_treatment(id):
    pass