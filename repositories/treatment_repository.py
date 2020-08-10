from db.run_sql import run_sql
from models.treatment import Treatment
import datetime
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

#CREATE
def save(treatment):
    sql = "INSERT INTO treatments (animal_id, vet_id, details, date) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [treatment.animal.id, treatment.vet.id, treatment.details, treatment.date]
    result = run_sql(sql, values)[0]
    id = result['id']
    treatment.id = id

#READ
def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        animal = animal_repository.select(row['animal_id'])
        treatment = Treatment(animal, vet, row['details'], row['date'], row['id'])
        treatments.append(treatment)

    return treatments

def select(id):
    sql = "SELECT * FROM treatments WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    vet = vet_repository.select(result['vet_id'])
    animal = animal_repository.select(result['animal_id'])
    treatment = Treatment(animal, vet, result['details'], result['date'], id)
    return treatment

#UPDATE
def update(treatment):
    sql = "UPDATE treatments SET (details, date) = (%s, %s) WHERE id=%s"
    values = [treatment.details, treatment.date, treatment.id]
    run_sql(sql, values)

#DELETE
def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM treatments WHERE id=%s"
    values = [id]
    run_sql(sql, values)