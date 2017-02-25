class Boy:
	def __init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_):
		self.name = name
		self.attractiveness = attractiveness
		self.boys_girlfriend_budget = girlfriend_budget
		self.intelligence = intelligence
		self.minimum_attraction_requirement = minimum_attraction_requirement
		self.type_=type_
		self.relationship_status = 'single'
		self.happiness=0
		self.girlfriend = ''
	
	def set_happiness(self,happiness) :
		self.happiness=happiness

	def set_girlfriend(self,girlfriend):
		self.girlfriend=girlfriend
	
	def modify_boys_girlfriend_budget(self,budget):
		self.boys_girlfriend_budget=budget
		
	def is_eligible(self, maintenance_budget, attractiveness):
		if (self.boys_girlfriend_budget >= maintenance_budget) and (attractiveness >= self.minimum_attraction_requirement):
			return True
		else:
			return False