import unittest

from script import somme, moyenne, ecart_type

class TestCalculs(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme([1, 2, 3]), 6)
    
    def test_moyenne(self):
        self.assertEqual(moyenne([1, 2, 3]), 2)
    
    def test_ecart_type(self):
        self.assertAlmostEqual(ecart_type([1, 2, 3]), 0.8165, places=4)

if __name__ == "__main__":
    unittest.main()

