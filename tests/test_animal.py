import unittest
import datetime
from models.animal import Animal
from models.vet import Vet

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal_1 = Animal("Tigger", datetime.date(2019,5,1), "Tiger", {'name': 'Carole Baskin', 'Phone':'07411287053'})
        self.vet_1 = Vet("John", "Smith")

    def test_intialisation_no_treatments_no_vet(self):
        self.assertEqual("Tigger", self.animal_1.name)
        self.assertEqual("2019-05-01", str(self.animal_1.dob))
        self.assertEqual("Tiger", self.animal_1.animal_type)
        self.assertEqual({'name': 'Carole Baskin', 'Phone':'07411287053'}, self.animal_1.owner_details)
        self.assertEqual({}, self.animal_1.treatment_notes)
        self.assertEqual(None, self.animal_1.vet)
        self.assertEqual(None, self.animal_1.id)

    def test_assign_vet(self):
        self.animal_1.assign_vet(self.vet_1)
        self.assertEqual(self.vet_1, self.animal_1.vet)