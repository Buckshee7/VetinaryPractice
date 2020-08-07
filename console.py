import pdb
import datetime
from models.vet import Vet
from models.animal import Animal
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

vet_repository.delete_all()

vet_1 = Vet("John", "Smith")
vet_2 = Vet("Vetty", "McVetface")

vet_repository.save(vet_1)
vet_repository.save(vet_2)

animal_1 = Animal("Tigger", datetime.date(2019,5,1), "Tiger", {'name': 'Carole Baskin', 'Phone':'07411287053'}, vet_1)

animal_repository.save(animal_1)

# vet_repository.delete(vet_1)

all_vets = vet_repository.select_all()

returned_vet = vet_repository.select(vet_2)
no_vet_returned = vet_repository.select(vet_1)

vet_1.first_name = "Will"
vet_repository.update(vet_1)
returned_vet_2 = vet_repository.select(vet_1)

pdb.set_trace()