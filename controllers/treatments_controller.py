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
    elif source == "animal":
        source_id = animal_repository.select(treatment.animal.id).id
    treatment_repository.delete(id)
    return redirect(f'/{source}s/{source_id}')

#<animal_id> is the source animal the treatment is being applied to - used for redirecting after addition
@treatments_blueprint.route('/treatments/new/<animal_id>')
def get_info_for_new(animal_id):
    animal = animal_repository.select(animal_id)
    vet = animal.vet
    return render_template('/treatments/new.html', animal=animal, vet=vet, title='New Treatment')

@treatments_blueprint.route('/treatments', methods=['POST'])
def create_new_treatment():
    animal_id = request.form['animal_id']
    animal = animal_repository.select(animal_id)
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    date = request.form['date']
    details = request.form['details']
    new_treatment = Treatment(animal, vet, details, date)
    treatment_repository.save(new_treatment)
    return redirect(f'/animals/{animal_id}')

@treatments_blueprint.route('/treatments/<id>/edit/<source>')
def get_info_for_update(id, source):
    treatment = treatment_repository.select(id)
    vet = vet_repository.select(treatment.vet.id)
    animal = animal_repository.select(treatment.animal.id)
    return render_template('treatments/edit.html', treatment=treatment, source=source, vet=vet, animal=animal, title='Update Treatment')

@treatments_blueprint.route('/treatments/<id>', methods=['POST'])
def update_treatment(id):
    animal_id = request.form['animal_id']
    animal = animal_repository.select(animal_id)
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    date = request.form['date']
    details = request.form['details']

    source = request.form['source']
    if source == "vet":
        source_id = vet.id
    elif source == "animal":
        source_id = animal.id

    updated_treatment = Treatment(animal, vet, details, date, id)
    treatment_repository.update(updated_treatment)
    return redirect(f'/{source}s/{source_id}')