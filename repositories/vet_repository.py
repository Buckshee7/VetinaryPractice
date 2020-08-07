from db.run_sql import run_sql
from models.vet import Vet

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

#UPDATE

#REMOVE