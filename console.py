import pdb
from models.vet import Vet
import repositories.vet_repository as vet_repository

vet_1 = Vet("John", "Smith")
vet_2 = Vet("Vetty", "McVetface")

vet_repository.save(vet_1)
vet_repository.save(vet_2)

all_vets = vet_repository.select_all()

pdb.set_trace()