from datetime import date

class Animal():
    def __init__(self, name, dob, animal_type, owner_name, owner_phone, vet = None, treatment_notes = "", id = None):
        self.name = name
        self.dob = dob
        self.animal_type = animal_type
        self.owner_name = owner_name
        self.owner_phone = owner_phone
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.id = id

    def assign_vet(self, Vet):
        self.vet = Vet

    #this method could be improved as doesnt incorporate leap years
    def calculate_age(self):
        age_days = date.today() - self.dob
        age_years = age_days.days // 365
        return age_years