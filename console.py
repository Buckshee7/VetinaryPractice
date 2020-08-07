import pdb
from models.vet import Vet
import repositories.vet_repository as vet_repository

vet_repository.delete_all()

vet_1 = Vet("John", "Smith")
vet_2 = Vet("Vetty", "McVetface")

vet_repository.save(vet_1)
vet_repository.save(vet_2)

# vet_repository.delete(vet_1)

all_vets = vet_repository.select_all()

returned_vet = vet_repository.select(vet_2)
no_vet_returned = vet_repository.select(vet_1)

vet_1.first_name = "Will"
vet_repository.update(vet_1)
returned_vet_2 = vet_repository.select(vet_1)

pdb.set_trace()