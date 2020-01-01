import unittest
from api_controller import ApiController
import json

class TestQ2Yak(unittest.TestCase):
	
	def setUp(self):
		self.api_controller = ApiController()
		pass

	def test_get_stock(self):
		expected_data_13 = { "milk": 1142.31,    "skins": 3}
		expected_data_14 = { "milk": 1229.55,    "skins": 6}
		res = self.api_controller.view_get_stock(13)
		self.assertEqual(res,expected_data_13)
		res = self.api_controller.view_get_stock(14)
		self.assertEqual(res,expected_data_14)

	def test_check_order(self):
		input_all_13 = json.dumps({"customer" : "Medvedev","order" : {"milk" : 1100,"skins" : 1} }).encode('utf-8')
		expected_all_13 = [{"milk" : 1100,"skins" : 1} , 201]
		res = self.api_controller.get_order( input_all_13, 13)
		self.assertEqual(res,expected_all_13)
		#################
		input_milk_13 = json.dumps({"customer" : "Medvedev","order" : {"milk" : 1100,"skins" : 7} }).encode('utf-8')
		expected_milk_13 = [{"milk" : 1100} , 206]		
		res = self.api_controller.get_order( input_milk_13, 13)
		self.assertEqual(res,expected_milk_13)
		# #################
		input_none_13 = json.dumps({"customer" : "Medvedev","order" : {"milk" : 1700,"skins" : 7} }).encode('utf-8')
		expected_none_13 = [{} , 404]		
		res = self.api_controller.get_order( input_none_13, 13)
		self.assertEqual(res,expected_none_13)

  