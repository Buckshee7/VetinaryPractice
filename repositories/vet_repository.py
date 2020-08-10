import datetime
from db.run_sql import run_sql
from models.vet import Vet
from models.animal import Animal
from models.treatment import Treatment
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.treatment_repository as treatment_repository
import repositories.vet_repository as vet_repository

#CREATE
def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, img_url) VALUES (%s, %s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name, vet.img_url]
    result = run_sql(sql, values)[0]
    id = result['id']
    vet.id = id

#READ
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['img_url'], row['id'])
        vets.append(vet)
    
    return vets

def select(vet_id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [vet_id]
    result = run_sql(sql, values)

    if result:
        vet_dict = result[0]
        vet = Vet(vet_dict['first_name'], vet_dict['last_name'], vet_dict['img_url'], vet_dict['id'])
        return vet

def animals(vet_id):
    animals = []
    sql = "SELECT * FROM animals WHERE vet_id = %s"
    values = [vet_id]
    results = run_sql(sql, values)

    for row in results:
        vet = select(row['vet_id']) if row['vet_id'] else None
        owner = owner_repository.select(row['owner_id'])
        animal = Animal(row['name'], row['dob'], row['animal_type'], owner, vet, row['img_url'], row['id'])
        animals.append(animal)
    
    return animals

def treatments(id):
    treatments = []
    sql = "SELECT * FROM treatments WHERE vet_id=%s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        animal = animal_repository.select(row['animal_id'])
        treatment = Treatment(animal, vet, row['details'], row['date'], row['id'])
        treatments.append(treatment)

    return treatments

#UPDATE
def update(vet):
    sql = "UPDATE vets SET (first_name, last_name, img_url) = (%s, %s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.img_url, vet.id]
    run_sql(sql, values)

#REMOVE
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(vet_id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [vet_id]
    run_sql(sql, values)