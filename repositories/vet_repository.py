import datetime
from db.run_sql import run_sql
from models.vet import Vet
from models.animal import Animal
import repositories.animal_repository as animal_repository

#CREATE
def save(vet):
    sql = "INSERT INTO vets (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name]
    result = run_sql(sql, values)[0]
    id = result['id']
    vet.id = id

#READ
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['id'])
        vets.append(vet)
    
    return vets

def select(vet_id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [vet_id]
    result = run_sql(sql, values)

    if result:
        vet_dict = result[0]
        vet = Vet(vet_dict['first_name'], vet_dict['last_name'], vet_dict['id'])
        return vet

def animals(vet_id):
    animals = []
    sql = "SELECT * from animals WHERE vet_id = %s"
    values = [vet_id]
    results = run_sql(sql, values)

    for row in results:
        dob = datetime.datetime.strptime(row['dob'], '%Y-%m-%d').date()
        vet = select(row['vet_id']) if row['vet_id'] else None
        animal = Animal(row['name'], dob, row['animal_type'], row['owner_details'], vet, row['id'])
        animals.append(animal)
    
    return animals

#UPDATE
def update(vet):
    sql = "UPDATE vets SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.id]
    run_sql(sql, values)

#REMOVE
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(vet_id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [vet_id]
    run_sql(sql, values)