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
        registered = True if row['registered'] == "True" else False
        owner = Owner(row['title'], row['first_name'], row['last_name'], registered, row['id'])
        owners.append(owner)
    
    return owners

#UPDATE


#DELETE