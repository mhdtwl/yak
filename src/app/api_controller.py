from application import  Application
from xml.dom import minidom
import json
import xml.etree.ElementTree as ET
import xmltodict


class ApiController(Application):
	"""docstring for ApiController"""
	
	def __init__(self):
		super(ApiController, self).__init__()
	## Q2
	def write_file(self, xml_data): #../data
		data = 	ET.fromstring(xml_data)
		xmlstr = '\n'.join([line for line in minidom
					.parseString(ET.tostring(data))
					.toprettyxml(indent="   ")
					.split('\n') if line.strip()])
		with open(self.xml_filepath, "w") as f:
		    f.write(xmlstr)
		pass
	## Q2
	def load(self, xml):
		"""Reset contents"""
		status = 205
		self.write_file(xml)
		return [xml,status]

	## Q3	
	def view_get_stock(self, T = 13):
		"""Reset contents"""
		result = self.yak_1_calculation(T)
		return  {"milk" : result['stock']['milk'] , "skins": result['stock']['wool'] }

	## Q3	
	def view_get_herd(self, T):
		"""Reset contents"""
		result = self.yak_1_calculation(T)
		return  json.dumps({'herd' : self.get_herd_list(result['list']) })
		
	#Q4
	def read_xmlfile_json(self, file): #../data
		tree = ET.parse(file)
		xml_data = tree.getroot()
		xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')
		data_dict = dict(xmltodict.parse(xmlstr))
		return data_dict 
	
	def compare_store_order_request(self, json_req, json_store):
		status=404
		response={}
		milk=False
		skin=False
		json_req_milk = json_req["order"]["milk"]
		json_req_skin = json_req["order"]["skins"]
		if json_req_milk <= json_store['milk']:
			milk=True	
		if json_req_skin <= json_store['skins']:
			skin=True	
		if milk and skin:
		    status = 201
		    response = {"milk" : json_req_milk , "skins": json_req_skin }
		elif milk or skin:
			status = 206
			if milk:
				response = {"milk" : json_req_milk }
			else:
				response = {"skins": json_req_skin }
		else:
			response = {}
		return [response, status]	


	def match_in_store(self, json_req, T):
		## calculate
		json_store_has = self.view_get_stock(T)
		## compare 
		return self.compare_store_order_request(json_req, json_store_has)

	def get_order(self, json_req, T = 13):
		"""order check"""
		self.T = T
		json_request = json.loads(json_req.decode('utf-8'))
		return self.match_in_store(json_request , T)
		#current_data = self.read_xmlfile_json(self.xml_filepath)

	
	
	








# @route('/')
# def f():
#     Response.status = 300 # also tried `Response.status_code = 300`
#     return dict(hello='world')

#import string, json, os	