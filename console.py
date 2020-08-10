import pdb
import datetime
from models.vet import Vet
from models.animal import Animal
from models.owner import Owner
from models.treatment import Treatment
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.treatment_repository as treatment_repository

treatment_repository.delete_all()
animal_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()

vet_1 = Vet("John", "Smith")
vet_2 = Vet("Vetty", "McVetface", "static/images/dr2.jpg")

vet_repository.save(vet_1)
vet_repository.save(vet_2)

owner_1 = Owner("Cpt.", "Jack", "Harkness", "0741000000", True)

owner_repository.save(owner_1)

owner_1.title = "Mjr."
owner_repository.update(owner_1)

all_owners = owner_repository.select_all()
returned_owner = owner_repository.select(owner_1.id)

# owner_repository.delete(owner_1.id)

animal_1 = Animal("Tigger", datetime.date(2017,5,1), "Tiger", owner_1)
animal_2 = Animal("Roger", datetime.date(2018,7,2), "Rabbit", owner_1, vet_1)

# animal_1_age = animal_1.calculate_age()

animal_repository.save(animal_1)
animal_repository.save(animal_2)

# vet_repository.delete(vet_1.id)

all_vets = vet_repository.select_all()

returned_vet = vet_repository.select(vet_2.id)
no_vet_returned = vet_repository.select(vet_1.id)

treatment_1 = Treatment(animal_1, vet_1, "Vaccination: COVID")
treatment_repository.save(treatment_1)

all_treatments = treatment_repository.select_all()

vet_1.first_name = "Will"
vet_repository.update(vet_1)
returned_vet_2 = vet_repository.select(vet_1.id)
animal_2.name = "Peter"
animal_repository.update(animal_2)

all_animals = animal_repository.select_all()
returned_animal = animal_repository.select(animal_2.id)

vet_1_animals = vet_repository.animals(vet_1.id)

pdb.set_trace()