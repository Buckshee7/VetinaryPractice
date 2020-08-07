import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet_1 = Vet("John", "Smith")
    
    def test_initialisation(self):
        self.assertEqual("John", self.vet_1.first_name)
        self.assertEqual("Smith", self.vet_1.last_name)
        self.assertEqual(None, self.vet_1.id)
