import unittest
import datetime
from models.animal import Animal

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal_1 = Animal("Tigger", datetime.date(2019,5,1), "Tiger", {'name': 'Carole Baskin', 'Phone':'07411287053'})

    def test_intialisation_no_treatments_no_vet(self):
        self.assertEqual("Tigger", self.animal_1.name)
        self.assertEqual("2019-05-01", self.animal_1.dob)
        self.assertEqual("Tiger", self.animal_1.animal_type)
        self.assertEqual({'name': 'Carole Baskin', 'Phone':'07411287053'}, self.animal_1.owner_details)
        self.assertEqual({}, self.animal_1.treatment_notes)
        self.assertEqual(None, self.animal_1.vet)