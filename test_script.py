import unittest

from script import somme, moyenne, ecart_type, minimum, maximum

class TestCalculs(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme([1, 2, 3]), 6)
    
    def test_moyenne(self):
        self.assertEqual(moyenne([1, 2, 3]), 2)
    
    def test_ecart_type(self):
        self.assertAlmostEqual(ecart_type([1, 2, 3]), 0.8165, places=4)

    def test_minimum(self):
        self.assertEqual(minimum([3, 1, 4]), 1)

    def test_maximum(self):
        self.assertEqual(maximum([3, 1, 4]), 4)

if __name__ == "__main__":
    unittest.main()

