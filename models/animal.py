from datetime import date

class Animal():
    def __init__(self, name, dob, animal_type, owner, vet = None, img_url = "static/images/no_img.jpg", id = None):
        self.name = name
        self.dob = dob
        self.animal_type = animal_type
        self.owner = owner
        self.vet = vet
        self.img_url = img_url
        self.id = id

    #this method could be improved as doesnt incorporate leap years
    def calculate_age(self):
        age_days = date.today() - self.dob
        age_years = age_days.days // 365
        return age_years