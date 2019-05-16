import unittest
from unittest.mock import patch
from math import pi
from hypothesis import given
import hypothesis.strategies as st
import Exercices as ex

class Exercice_1_Test_case(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_positif(self, x, y):
        # print(f"x = {x} et y = {y}")
        self.assertEqual(ex.exercice_1(x, y), x*y)

    @given(st.integers(), st.integers())
    def test_negatif(self, x, y):
        self.assertEqual(ex.exercice_1(-x, y), -x*y)

    def test_nul(self):
        self.assertEqual(ex.exercice_1(0, 200), 0)
        self.assertEqual(ex.exercice_1(0, 0), 0)
        self.assertEqual(ex.exercice_1(0, -500), 0)

    def test_str(self):
        self.assertRaises(TypeError, ex.exercice_1, "abc", "def")
        self.assertRaises(TypeError, ex.exercice_1, "abc", 0)
        self.assertRaises(TypeError, ex.exercice_1, 10, "")

class Exercice_2_Test_case(unittest.TestCase):

    def test_inf(self):
        self.assertEqual(ex.exercice_2(-2, 1, 2), -255)
        self.assertEqual(ex.exercice_2(-1000, 10, 15), -255)
        self.assertEqual(ex.exercice_2(-10, -5, 2), -255)
        self.assertEqual(ex.exercice_2(-15, -10, -2), -255)

    def test_in(self):
        self.assertEqual(ex.exercice_2(1, 1, 2), 1)
        self.assertEqual(ex.exercice_2(2, 1, 2), 2)
        self.assertEqual(ex.exercice_2(5, 1, 10), 5)
        self.assertEqual(ex.exercice_2(-5, -6, 2), -5)

    def test_sup(self):
        self.assertEqual(ex.exercice_2(3, 1, 2), 255)
        self.assertEqual(ex.exercice_2(5, -1, 2), 255)
        self.assertEqual(ex.exercice_2(-2, -10, -5), 255)
        self.assertEqual(ex.exercice_2(5, 2, 2), 255)

    def test_str(self):
        self.assertRaises(TypeError, ex.exercice_2, "abc", "def", "ghi")
        self.assertRaises(TypeError, ex.exercice_2, "abc", 0, 2)
        self.assertRaises(TypeError, ex.exercice_2, 10, "", "abc")

class Exercice_3_Test_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Début")

    @classmethod
    def tearDownClass(cls):
        print("Fin")
    
    def setUp(self):
        self.exo = ex.Exercice_3()

    def tearDown(self):
        print("Fin du test")
    
    def test_r_num(self):
        self.assertEqual(self.exo.r_num(10), None)
        self.assertEqual(self.exo.r, 10)
        self.assertRaises(TypeError, self.exo.r_num, "abc")
        self.assertRaises(ValueError, self.exo.r_num, -5)

    def test_aire(self):
        self.assertAlmostEqual(self.exo.aire(10), pi*10**2)
        self.assertEqual(self.exo.aire(0), 0)
        self.assertRaises(TypeError, self.exo.aire, "abc")
        self.assertRaises(ValueError, self.exo.aire, -8)

    def test_perimetre(self):
        self.assertAlmostEqual(self.exo.perimetre(5), 2*pi*5)
        self.assertEqual(self.exo.perimetre(0), 0)
        self.assertRaises(TypeError, self.exo.perimetre, "abc")
        self.assertRaises(ValueError, self.exo.perimetre, -8)

    def test_dans_cercle(self):
        self.assertTrue(self.exo.dans_cercle(2, 0, 1))
        self.assertTrue(self.exo.dans_cercle(2, 1, 0))
        self.assertTrue(self.exo.dans_cercle(2, 1, 1))
        self.assertTrue(self.exo.dans_cercle(2, -1, -1))
        self.assertFalse(self.exo.dans_cercle(2, 2, 2))
        self.assertFalse(self.exo.dans_cercle(2, -3, 2))
        self.assertRaises(TypeError, self.exo.dans_cercle, "abc", 3, 4)
        self.assertRaises(TypeError, self.exo.dans_cercle, 8, "abc", 4)
        self.assertRaises(TypeError, self.exo.dans_cercle, 8, 56, "abc")
        self.assertRaises(ValueError, self.exo.dans_cercle, -8, 2, 3)
    
class Exercice_4_Test_case(unittest.TestCase):

    def test_init(self):
        with patch("Exercices.requests.get") as mocked_get:
            exo = ex.Exercice_4("Paris")
            mocked_get.assert_called_with("https://fr.wikipedia.org/w/api.php",
                                          params={
                                                "search": "Paris",
                                                "format": "json",
                                                "action": "opensearch", 
                                              })
    def test_loc(self):
        with patch("Exercices.requests.get") as mocked_get:
            mocked_get.return_value.text = "la ville de Lyon"
            exo = ex.Exercice_4("Lyon")
            self.assertEqual(exo.loc(), "Voici ce que je connais de Lyon : la ville de Lyon")
        
if __name__=="__main__":
    unittest.main()
