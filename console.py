import pdb
from models.vet import Vet
import repositories.vet_repository as vet_repository

vet_1 = Vet("John", "Smith")
vet_repository.save(vet_1)

pdb.set_trace()