from flask import Blueprint, render_template, redirect, request
import repositories.owner_repository as owner_repository
from models.owner import Owner

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route('/owners')
def index():
    pass

@owners_blueprint.route('/owners/<id>')
def show(id):
    pass

@owners_blueprint.route('/owners/<id>/delete')
def delete(id):
    pass

@owners_blueprint.route('/owners/new')
def get_info_for_new():
    pass

@owners_blueprint.route('/owners', methods=['POST'])
def create_new_owner():
    pass

@owners_blueprint.route('/owners/<id>/edit')
def get_info_for_update(id):
    pass

@owners_blueprint.route('/owners/<id>', methods=['POST'])
def update_owner(id):
    pass