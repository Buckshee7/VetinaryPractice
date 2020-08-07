from db.run_sql import run_sql

#CREATE
def save(vet):
    sql = "INSERT INTO vets (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name]
    result = run_sql(sql, values)[0]
    id = result['id']
    vet.id = id

#READ

#UPDATE

#REMOVE