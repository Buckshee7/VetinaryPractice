from flask import Blueprint, render_template, request, redirect
import repositories.treatment_repository as treatment_repository
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

@treatments_blueprint.route('/treatments/<id>/delete')
def delete(id):
    pass

@treatments_blueprint.route('/treatments/new')
def get_info_for_new():
    pass

@treatments_blueprint.route('/treatments', methods=['POST'])
def create_new_vet():
    pass

@treatments_blueprint.route('/treatments/<id>/edit')
def get_info_for_update(id):
    pass

@treatments_blueprint.route('/treatments/<id>', methods=['POST'])
def update_treatment(id):
    pass