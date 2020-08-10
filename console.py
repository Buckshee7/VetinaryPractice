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

owner_1 = Owner('Mr', 'Thomas', 'Tankengine', '07411000000', True)
owner_2 = Owner('Mrs', 'Euphegenia', 'Doubtfire', '07411000000', True)
owner_3 = Owner('Ms', 'Wilma', 'Flintstone', '07411000000', False)
owner_4 = Owner('Cpt', 'Malcolm', 'Reynolds', '07411000000', False)

owner_repository.save(owner_1)
owner_repository.save(owner_2)
owner_repository.save(owner_3)
owner_repository.save(owner_4)

vet_1 = Vet('Vetty', 'McVetface', 'static/images/dr1.jpg')
vet_2 = Vet('Ace', 'Ventura', 'static/images/dr2.jpg')
vet_3 = Vet('Rolf', 'Harris', 'static/images/dr3.jpg')
vet_4 = Vet('Brian', 'Cox')

vet_repository.save(vet_1)
vet_repository.save(vet_2)
vet_repository.save(vet_3)
vet_repository.save(vet_4)

animal_1 = Animal('Rafiki', datetime.datetime(2015, 1, 10).date(), 'Monkey', owner_1, vet_1, 'static/images/monkey.jpg')
animal_2 = Animal('Rufus', datetime.datetime(2016, 2, 10).date(), 'Dog', owner_1, vet_2, 'static/images/dog.jpg')
animal_3 = Animal('Nemo', datetime.datetime(2017, 3, 10).date(), 'Fish', owner_1, vet_3)
animal_4 = Animal('Tigger', datetime.datetime(2018, 4, 10).date(), 'Tiger', owner_2, vet_1, 'static/images/tiger.jpg')
animal_5 = Animal('Peter', datetime.datetime(2019, 5, 10).date(), 'Rabbit', owner_2, vet_1, 'static/images/rabbit.jpg')
animal_6 = Animal('Baloo', datetime.datetime(2020, 6, 10).date(), 'Bear', owner_3, vet_2, 'static/images/bear.jpg')
animal_7 = Animal('Sheldon', datetime.datetime(2016, 7, 10).date(), 'Turtle', owner_4, vet_1)
animal_8 = Animal('Notahorse', datetime.datetime(2010, 8, 10).date(), 'Unicorn', owner_4, None, 'static/images/unicorn.jpg')
animal_9 = Animal('Trogdor', datetime.datetime(1800, 9, 10).date(), 'Dragon', owner_4, None, 'static/images/dragon.jpg')
animal_10 = Animal('Barney', datetime.datetime(1992, 10, 10).date(), 'T-rex', owner_4, vet_2,)

animal_repository.save(animal_1)
animal_repository.save(animal_2)
animal_repository.save(animal_3)
animal_repository.save(animal_4)
animal_repository.save(animal_5)
animal_repository.save(animal_6)
animal_repository.save(animal_7)
animal_repository.save(animal_8)
animal_repository.save(animal_9)
animal_repository.save(animal_10)

treatment_1 = Treatment(animal_1, vet_1, "Vaccination: COVID First Shot", datetime.datetime(2020, 8, 10).date())
treatment_2 = Treatment(animal_1, vet_1, "Vaccination: COVID Second Shot", datetime.datetime(2020, 8, 11).date())
treatment_3 = Treatment(animal_1, vet_1, "Check-up: General", datetime.datetime(2020, 8, 12).date())
treatment_4 = Treatment(animal_1, vet_1, "De-fleaing", datetime.datetime(2020, 8, 13).date())
treatment_5 = Treatment(animal_1, vet_1, "Treatment for banana-addiction", datetime.datetime(2020, 8, 14).date())
treatment_6 = Treatment(animal_1, vet_1, "Check-up: General", datetime.datetime(2020, 8, 15).date())
treatment_7 = Treatment(animal_2, vet_2, "Shell polishing", datetime.datetime(2020, 8, 10).date())
treatment_8 = Treatment(animal_2, vet_2, "Vaccination: COVID First Shot", datetime.datetime(2020, 8, 11).date())
treatment_9 = Treatment(animal_3, vet_3, "Couldn't find him", datetime.datetime(2020, 8, 12).date())
treatment_10 = Treatment(animal_4, vet_1, "Possible ADHD", datetime.datetime(2020, 8, 13).date())
treatment_11 = Treatment(animal_5, vet_1, "Treatment for carrot-addiction", datetime.datetime(2020, 8, 14).date())
treatment_12 = Treatment(animal_6, vet_2, "Reports of itchy back", datetime.datetime(2020, 8, 15).date())
treatment_13 = Treatment(animal_7, vet_1, "Vaccination: COVID First Shot", datetime.datetime(2020, 8, 10).date())
treatment_14 = Treatment(animal_8, vet_4, "Glueing on Horn", datetime.datetime(2020, 8, 11).date())
treatment_15 = Treatment(animal_9, vet_3, "Treat for 2nd degreee burns", datetime.datetime(2020, 8, 12).date())
treatment_16 = Treatment(animal_2, vet_2, "De-fleaing", datetime.datetime(2020, 8, 13).date())
treatment_17 = Treatment(animal_3, vet_3, "Reporting memory issues", datetime.datetime(2020, 8, 14).date())
treatment_18 = Treatment(animal_4, vet_1, "Vaccination", datetime.datetime(2020, 8, 15).date())
treatment_19 = Treatment(animal_5, vet_1, "Dental work", datetime.datetime(2020, 8, 10).date())
treatment_20 = Treatment(animal_8, vet_4, "Therapy: Believes is magical", datetime.datetime(2020, 8, 11).date())

treatment_repository.save(treatment_1)
treatment_repository.save(treatment_2)
treatment_repository.save(treatment_3)
treatment_repository.save(treatment_4)
treatment_repository.save(treatment_5)
treatment_repository.save(treatment_6)
treatment_repository.save(treatment_7)
treatment_repository.save(treatment_8)
treatment_repository.save(treatment_9)
treatment_repository.save(treatment_10)
treatment_repository.save(treatment_11)
treatment_repository.save(treatment_12)
treatment_repository.save(treatment_13)
treatment_repository.save(treatment_14)
treatment_repository.save(treatment_15)
treatment_repository.save(treatment_16)
treatment_repository.save(treatment_17)
treatment_repository.save(treatment_18)
treatment_repository.save(treatment_19)
treatment_repository.save(treatment_20)

pdb.set_trace()