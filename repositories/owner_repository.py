from db.run_sql import run_sql
from models.owner import Owner
from models.animal import Animal
import datetime

#CREATE
def save(owner):
    sql = "INSERT INTO owners (title, first_name, last_name, phone, registered) VALUES (%s, %s, %s, %s, %s) returning id"
    values = [owner.title, owner.first_name, owner.last_name, owner.phone, owner.registered]
    result = run_sql(sql, values)[0]
    owner.id = result['id']

#READ
def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['title'], row['first_name'], row['last_name'], row['phone'], row['registered'], row['id'])
        owners.append(owner)
    
    return owners

def select(id):
    sql = "SELECT * FROM owners WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        owner_dict = result[0]
        owner = Owner(owner_dict['title'], owner_dict['first_name'], owner_dict['last_name'], owner_dict['phone'], owner_dict['registered'], owner_dict['id'])
        return owner

def animals(owner):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id=%s"
    values = [owner.id]
    results = run_sql(sql, values)

    for row in results:
        dob = datetime.datetime.strptime(row['dob'], '%Y-%m-%d').date()
        vet = select(row['vet_id']) if row['vet_id'] else None
        owner = select(row['owner_id'])
        animal = Animal(row['name'], dob, row['animal_type'], owner, vet, row['img_url'], row['id'])
        animals.append(animal)
    
    return animals

#UPDATE
def update(owner):
    sql = "UPDATE owners SET (title, first_name, last_name, phone, registered) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [owner.title, owner.first_name, owner.last_name, owner.phone, owner.registered, owner.id]
    run_sql(sql, values)

#DELETE
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id=%s"
    values = [id]
    run_sql(sql, values)