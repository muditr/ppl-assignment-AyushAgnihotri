import random
import csv

def testing_util():
	
	gift_types = ['Essential','Luxury','Utiltiy']
	boy_types = ['Miser','Generous','Geek']
	girl_types = ['Choosy','Normal','Desperate']
	
	boys=[]
	girls=[]
	gifts=[]

	for i in range (0,100):
		boys+= [('Boy'+str(i),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100), boy_types[random.randint(0,2)])]

	for j in range (0,10):
		girls+=[('Girl'+str(j),random.randint(0,20),random.randint(0,20),random.randint(0,20), girl_types[random.randint(0,2)])]

	for k in range (0,11):
		gifts += [('Gift'+ str(k),random.randint(0,100),random.randint(0,100),gift_types[random.randint(0,2)])]
	
	create('./boys_list.csv',boys)
	create('./girls_list.csv',girls)
	create('./gifts_list.csv',gifts)


def create(file_name, list_name):
	fp = open(file_name, 'w')
	writer = csv.writer(fp, delimiter = ',')

	for i in list_name:
		writer.writerow(i)	

testing_util() 
