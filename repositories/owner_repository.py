from db.run_sql import run_sql
from models.owner import Owner

#CREATE
def save(owner):
    sql = "INSERT INTO owners (title, first_name, last_name, registered) VALUES (%s, %s, %s, %s) returning id"
    values = [owner.title, owner.first_name, owner.last_name, owner.registered]
    result = run_sql(sql, values)[0]
    owner.id = result['id']

#READ
def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['title'], row['first_name'], row['last_name'], row['registered'], row['id'])
        owners.append(owner)
    
    return owners

def select(id):
    sql = "SELECT * FROM owners WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        owner_dict = result[0]
        owner = Owner(owner_dict['title'], owner_dict['first_name'], owner_dict['last_name'], owner_dict['registered'], owner_dict['id'])
        return owner

#UPDATE


#DELETE
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)