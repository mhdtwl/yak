import xml.etree.ElementTree as ET
import json

class Labyak(object):
	"""docstring for Labyak"""
	name=""
	age=0
	sex=""
	
	# self.RATIO_YEAR_DAYS = 0.01
	# self.RATIO_DAYS_IN_YEAR = 100

	def __init__(self, name, age, sex):
		super(Labyak, self).__init__()
		self.name = name
		self.age = age
		self.sex = sex
	
	def get_json_yak3(self, T):
		""" return data of q3"""
		return {
		"name" : self.name, 
		"age" : self.age, 
		"age-last-shaved" : ((self.age * 100) - T)}
		 
		
	#name="Betty-1" age="4" sex="f"
	#age-last-shaved : 9.5

class Application(object):
	"""docstring for Application"""
	herd = [] 
	T = 0
	xml_filepath = "../data/data.xml"
	
	def __init__(self):
		super(Application, self).__init__()
	
	def file_reader(self, file_path):
		return ET.parse(file_path).getroot()
		
	def yak_data_reader(self, root_xml):
		herd_list = [] # root_xml.findall('labyak')
		for type_tag in root_xml.findall('labyak'):
		    name = type_tag.get('name')
		    age = float(type_tag.get('age'))
		    sex = type_tag.get('sex')
		    labyak = Labyak(name, age, sex)
		    herd_list.append(labyak)
		return herd_list

	def age_calculation(self, age, day_indexT):
		return ((age * 100 ) + day_indexT)/100
	################  MILK Calculation ###  50 - D * 0.03 #############
	def calc_milk_liters_per_labyak(self, labyak_age):
		""" return liters_at_an_age for certain Labyak """
		days = labyak_age * 100 # each year is 100 days 
		return 50 - (days * 0.03)

	def get_milk_liters_per_labyak_in_period(self, Labyak):
		liters = 0 
		for day_index in range(1, self.T+1):
			age = self.age_calculation(Labyak.age, day_index)
			## Todo  age_validation here & if Female
			liters += self.calc_milk_liters_per_labyak(age)
			pass
		return liters
 
	def calc_milk_liters_all(self, labyak_list):
		liters = 0 
		for labyak in labyak_list:
			liters += self.get_milk_liters_per_labyak_in_period(labyak)
			pass
		return liters

	################  WOOL Calculation  ### 8 + D * 0.01 ############
	def calc_skin_wool_per_labyak(self,  labyak_age):
		""" return skins_at_an_age for certain Labyak """
		days = labyak_age * 100 # each year is 100 days 
		return 8 - (days * 0.01)

	def get_wool_skins_per_labyak_in_period(self, Labyak):
		skins = 0 
		for day_index in range(1, self.T+1):
			age = self.age_calculation(Labyak.age, day_index)
			## Todo  age_validation here
			skins += self.calc_skin_wool_per_labyak(age) 
			pass
		return skins

	def calc_wool_skins_all(self, labyak_list):
		skins = 0 
		for labyak in labyak_list:
			skins += (self.get_wool_skins_per_labyak_in_period(labyak) )
			pass
		return int (skins % 13  )

	################  Stock ################
	def get_in_stock(self, labyak_list):
		liters = "0"
		skins = "0"
		liters = self.calc_milk_liters_all(labyak_list)
		skins = self.calc_wool_skins_all(labyak_list)
		return {'milk' : liters , 'wool' : skins}

	def get_herd(self, yak_list):
		#print(yak_list[0])
		herd = []
		days_plus = self.T * 0.01 
		for labyak in yak_list:
			## todo check age validation 
			name =  labyak.name
			age  =  labyak.age + days_plus
			sex  =  labyak.sex
			newlabyak = Labyak(name, age, sex)
			herd.append(newlabyak)
		return herd

	def get_herd_list(self, yak_list):
		json_list = []
		for yak in yak_list:
			json_list.append(yak.get_json_yak3(self.T))
			pass
		return json_list #json.dumps(json_list)
	################  1st Question ################
	def yak_1_operation(self, yak_list):
		stock = self.get_in_stock(yak_list)
		res_yak_list = self.get_herd(yak_list)
		return {'stock' : stock , 'list' : res_yak_list}

	def yak_1_calculation(self, T ):
		# read data
		self.T = T
		root_xml = self.file_reader(self.xml_filepath)  
		yak_list = self.yak_data_reader(root_xml)
		# calcuate 
		return self.yak_1_operation(yak_list)

	def yak_1(self, T = 13):
		"""Inputs: xml has the data. T : representing the elapsed time in days.
			Output: In stock list & Herd list"""
		self.T = T
		result = self.yak_1_calculation(T)
		# print
		self.yak_1_print_preparation(result['stock'], result['list'])
		pass

	def yak_1_print_preparation(self, stock, yak_list):
		print("In Stock:")
		print("\t" + str(stock['milk']) + " liters of milk")
		print("\t" + str(stock['wool']) + " skins of wool")
		print("Herd:")

		for yak in yak_list:
			print("\t"  + str(yak.name) + " " + str(yak.age) + " years old")
			pass
		pass	
