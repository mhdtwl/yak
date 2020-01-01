import unittest
from application import Application, Labyak

class TestQ1Yak(unittest.TestCase):
	
	def setUp(self):
		self.app = Application()
		pass

	def test_calc_age(self):
		res = self.app.age_calculation(11,13)
		self.assertAlmostEqual(res,11.13)

		res = self.app.age_calculation(8,16)
		self.assertAlmostEqual(res,8.16)

		res = self.app.age_calculation(7,16)
		self.assertNotEqual(res,8.10)

	def test_calc_milk(self):
		labyak1 = Labyak("Betty-1", 4, "f")
		labyak2 = Labyak("Betty-2", 8, "f")
		labyak3 = Labyak("Betty-3", 9.5, "f")
		labyak4 = Labyak("Betty-4", 9.5, "f")
		self.app.T = 13 
		res = self.app.calc_milk_liters_all([labyak1,labyak2,labyak3])
		self.assertEqual(res,1103.31)
		res = self.app.calc_milk_liters_all([labyak1,labyak2,labyak3,labyak4])
		self.assertEqual(res,1380.08)

	def test_calc_wool(self):
		labyak1 = Labyak("Betty-1", 4, "f")
		labyak2 = Labyak("Betty-2", 8, "f")
		labyak3 = Labyak("Betty-3", 9.5, "f")
		labyak4 = Labyak("Betty-4", 9.5, "f")
		self.app.T = 13 
		res = self.app.calc_wool_skins_all([labyak1,labyak2,labyak3])
		self.assertEqual(res,3)
		res = self.app.calc_wool_skins_all([labyak1,labyak2,labyak3,labyak4])
		self.assertEqual(res,9)
