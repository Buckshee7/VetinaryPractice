from db.run_sql import run_sql
from models.treatment import Treatment
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

#CREATE
def save(treatment):
    sql = "INSERT INTO treatments (animal_id, vet_id, details) VALUES (%s, %s, %s) RETURNING id"
    values = [treatment.animal.id, treatment.vet.id, treatment.details]
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
        treatment = Treatment(animal, vet, row['details'], row['id'])
        treatments.append(treatment)

    return treatments

#UPDATE


#DELETE
def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)