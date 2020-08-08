import datetime
from db.run_sql import run_sql
from models.animal import Animal
import repositories.vet_repository as vet_repository

#CREATE
def save(animal):
    vet_id = animal.vet.id if animal.vet else None
    sql = "INSERT INTO animals (name, dob, animal_type, owner_name, owner_phone, treatment_notes, vet_id, img_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [animal.name, str(animal.dob), animal.animal_type, animal.owner_name, animal.owner_phone, animal.treatment_notes, vet_id, animal.img_url]
    result = run_sql(sql, values)[0]
    animal.id = result['id']

#READ
def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        dob = datetime.datetime.strptime(row['dob'], '%Y-%m-%d').date()
        vet = vet_repository.select(row['vet_id']) if row['vet_id'] else None
        animal = Animal(row['name'], dob, row['animal_type'], row['owner_name'], row['owner_phone'], vet, row['img_url'], row['treatment_notes'], row['id'])
        animals.append(animal)
    
    return animals

def select(animal_id):
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [animal_id]
    result = run_sql(sql, values)

    if result:
        dict_animal = result[0]
        dob = datetime.datetime.strptime(dict_animal['dob'], '%Y-%m-%d').date()
        vet = vet_repository.select(dict_animal['vet_id']) if dict_animal['vet_id'] else None
        animal = Animal(dict_animal['name'], dob, dict_animal['animal_type'], dict_animal['owner_name'], dict_animal['owner_phone'], vet, dict_animal['img_url'], dict_animal['treatment_notes'], dict_animal['id'])
        return animal

#UPDATE
def update(animal):
    vet_id = animal.vet.id if animal.vet else None
    sql = "UPDATE animals SET (name, dob, animal_type, owner_name, owner_phone, treatment_notes, vet_id, img_url) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, str(animal.dob), animal.animal_type, animal.owner_name, animal.owner_phone, animal.treatment_notes, vet_id, animal.img_url, animal.id]
    run_sql(sql, values)


#DELETE
def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(animal_id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [animal_id]
    run_sql(sql, values)