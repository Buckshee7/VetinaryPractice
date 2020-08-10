from flask import Blueprint, render_template, request, redirect
import repositories.treatment_repository as treatment_repository
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import datetime
from models.treatment import Treatment

treatments_blueprint = Blueprint("treatments", __name__)

#route for delete FROM <source> page
@treatments_blueprint.route('/treatments/<id>/delete/<source>')
def delete_from_vet(id, source):
    treatment = treatment_repository.select(id)
    if source == "vet":
        source_id = vet_repository.select(treatment.vet.id).id
    else:
        source_id = animal_repository.select(treatment.animal.id).id
    treatment_repository.delete(id)
    return redirect(f'/{source}s/{source_id}')

@treatments_blueprint.route('/treatments/new/<source>')
def get_info_for_new(source):
    return render_template('/treatments/new.html', source=source, title='New Treatment')

@treatments_blueprint.route('/treatments', methods=['POST'])
def create_new_vet():
    pass

@treatments_blueprint.route('/treatments/<id>/edit')
def get_info_for_update(id):
    pass

@treatments_blueprint.route('/treatments/<id>', methods=['POST'])
def update_treatment(id):
    pass