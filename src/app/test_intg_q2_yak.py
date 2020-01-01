import unittest
#from api_controller import ApiController
from q2_yak import app
import json
import requests 


class TestQ2YakIntegration(unittest.TestCase):
	
	def setUp(self):
		self.base_url = 'http://localhost:5000/'
		pass

	def test_get_stock(self):
		res = requests.get(self.base_url + 'yak-shop/stock/13' )
		self.assertEqual(res.status_code,200)
		self.assertEqual(json.dumps(res.json()),'{"milk": 1142.31, "skins": 3}')
		res = requests.get(self.base_url + 'yak-shop/stock/14' )
		self.assertEqual(res.status_code,200)
		self.assertEqual(json.dumps(res.json()),'{"milk": 1229.55, "skins": 6}')

	 
	def test_check_order(self):
		url_order = 'yak-shop/order/13'
		#################
		input_all_13 = json.dumps({"customer" : "Medvedev","order" : {"milk" : 1100,"skins" : 1} }).encode('utf-8')
		expected_all_13 = '{"milk": 1100, "skins": 1}'
		res = requests.post(self.base_url + url_order, input_all_13 ) 
		self.assertEqual(res.status_code,201)
		self.assertEqual(json.dumps(res.json()), expected_all_13)
		#################
		input_milk_13 = json.dumps({"customer" : "Medvedev","order" : {"milk" : 1100,"skins" : 7} }).encode('utf-8')
		expected_milk_13 = '{"milk": 1100}'  	
		res = requests.post(self.base_url + url_order, input_milk_13) 
		self.assertEqual(res.status_code,206)
		self.assertEqual(json.dumps(res.json()), expected_milk_13)
		# # #################
		input_none_13 = json.dumps({"customer" : "Medvedev","order" : {"milk" : 1700,"skins" : 7} }).encode('utf-8')
		expected_none_13 = '{}'		
		res = requests.post(self.base_url + url_order, input_none_13) 
		self.assertEqual(res.status_code,404)
		self.assertEqual(json.dumps(res.json()),expected_none_13)

  