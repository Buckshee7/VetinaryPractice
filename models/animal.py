class Animal():
    def __init__(self, name, dob, animal_type, owner_details, treatment_notes = {}, vet = None, id = None):
        self.name = name
        self.dob = dob
        self.animal_type = animal_type
        self.owner_details = owner_details
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.id = id

    def assign_vet(self, Vet):
        self.vet = Vet