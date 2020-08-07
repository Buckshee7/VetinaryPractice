from flask import Blueprint
import repositories.animal_repository as animal_repository

animals_blueprint = Blueprint("animals", __name__)