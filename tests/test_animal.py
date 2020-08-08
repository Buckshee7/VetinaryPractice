import unittest
import datetime
from models.animal import Animal
from models.vet import Vet

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.vet_1 = Vet("John", "Smith")
        self.animal_1 = Animal("Tigger", datetime.date(2019,5,1), "Tiger", 'Carole Baskin', '07411287053')
        self.animal_2 = Animal("Roger", datetime.date(2018,7,2), "Rabbit", 'Elmer Fudd', '014100000000', self.vet_1)

    def test_intialisation_no_treatments_no_vet(self):
        self.assertEqual("Tigger", self.animal_1.name)
        self.assertEqual("2019-05-01", str(self.animal_1.dob))
        self.assertEqual("Tiger", self.animal_1.animal_type)
        self.assertEqual('Carole Baskin', self.animal_1.owner_name)
        self.assertEqual("", self.animal_1.treatment_notes)
        self.assertEqual(None, self.animal_1.vet)
        self.assertEqual(None, self.animal_1.id)

    def test_calculate_age_1(self):
        self.assertEqual(1, self.animal_1.calculate_age())

    def test_calculate_age_2(self):
        self.assertEqual(2, self.animal_2.calculate_age())