from datetime import date

class Animal():
    def __init__(self, name, dob, animal_type, owner_details, vet = None, id = None):
        self.name = name
        self.dob = dob
        self.animal_type = animal_type
        self.owner_details = owner_details
        self.treatment_notes = {}
        self.vet = vet
        self.id = id

    def assign_vet(self, Vet):
        self.vet = Vet

    #this method could be improved as doesnt incorporate leap years
    def calculate_age(self):
        age_days = date.today() - self.dob
        age_years = age_days.days // 365
        return age_years