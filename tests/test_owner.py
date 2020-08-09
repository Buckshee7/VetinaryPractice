import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner_1 = Owner("Cpt.", "Jack", "Harkness", True)
    
    def test_initialisation(self):
        self.assertEqual("Jack", self.owner_1.first_name)
        self.assertEqual("Harkness", self.owner_1.last_name)
        self.assertEqual(True, self.owner_1.registered)
        self.assertEqual(None, self.owner_1.id)
