from flask import Blueprint, render_template, request, redirect
import repositories.treatment_repository as treatment_repository
import datetime
from models.treatment import Treatment

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route('/treatments/<id>')
def show(id):
    pass

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