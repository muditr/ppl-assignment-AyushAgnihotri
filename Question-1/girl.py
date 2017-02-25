class girl:
	def __init__(self,name,attractiveness,maintenance_budget,intelligence,type_):
		self.name = name
		self.maintenance_budget = maintenance_budget
		self.intelligence = intelligence
		self.attractiveness = attractiveness
		self.relationship_status = 'single'
		self.boyfriend = ''
		self.happiness=0
		self.type_=type_

	def set_happiness(self,happiness) :
		self.happiness=happiness

	def set_girlfriend(self,girlfriend):
		self.girlfriend=girlfriend

	def modify_maintenance_budget(self,budget):
		self.maintenance_budget=budget
	
	def is_eligible(self, boys_girlfriend_budget):
		if (self.maintenance_budget <= boys_girlfriend_budget):
			return True
		else:
			return False
