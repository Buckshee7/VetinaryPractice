from db.run_sql import run_sql
from models.animal import Animal

#CREATE
def save(animal):
    vet_id = animal.vet.id if animal.vet else None
    sql = "INSERT INTO animals (name, dob, animal_type, owner_details, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [animal.name, str(animal.dob), animal.animal_type, str(animal.owner_details), str(animal.treatment_notes), vet_id]
    result = run_sql(sql, values)[0]
    animal.id = result['id']
    
#READ


#UPDATE


#DELETE
