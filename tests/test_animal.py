import unittest
import datetime
from models.animal import Animal
from models.vet import Vet
from models.owner import Owner

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.vet_1 = Vet("John", "Smith")
        self.owner_1 = Owner("Cpt.", "Jack", "Harkness", "07411000000", True)
        self.animal_1 = Animal("Tigger", datetime.date(2019,5,1), "Tiger", self.owner_1)
        self.animal_2 = Animal("Roger", datetime.date(2018,7,2), "Rabbit", self.owner_1, self.vet_1)

    def test_intialisation_no_treatments_no_vet(self):
        self.assertEqual("Tigger", self.animal_1.name)
        self.assertEqual("2019-05-01", str(self.animal_1.dob))
        self.assertEqual("Tiger", self.animal_1.animal_type)
        self.assertEqual(self.owner_1, self.animal_1.owner)
        self.assertEqual(None, self.animal_1.vet)
        self.assertEqual(None, self.animal_1.id)

    def test_calculate_age_1(self):
        self.assertEqual(1, self.animal_1.calculate_age())

    def test_calculate_age_2(self):
        self.assertEqual(2, self.animal_2.calculate_age())