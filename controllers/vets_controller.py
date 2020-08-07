from flask import Blueprint, render_template
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def index():
    vets = vet_repository.select_all()
    return render_template('/vets/index.html', vets=vets, title='Vets')