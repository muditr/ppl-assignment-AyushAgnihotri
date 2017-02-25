import csv

from girl import girl
from boy import Boy
from util import testing_util
from logs import log_maker

testing_util()
boys = open('./boys_list.csv')
getboy = csv.reader(boys, delimiter = ',')
girls = open('./girls_list.csv')
getgirl = csv.reader(girls, delimiter = ',')
boy_list=[]
girl_list=[]

for i in getboy:
	boy_list += [Boy(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])] 

for j in getgirl:
	girl_list += [girl(j[0],int(j[1]),int(j[2]),int(j[3]),j[4])]

for k in  girl_list:
	for l in  boy_list:
		log_maker(k.name + '  is looking for  ' + l.name)
		if l.relationship_status=='single' and k.relationship_status=='single' and k.is_eligible(l.boys_girlfriend_budget) and l.is_eligible(k.maintenance_budget, k.attractiveness) :
			l.girlfriend = k.name
			k.boyfriend = l.name
			l.relationship_status= 'In_a_relationship'
			k.relationship_status = 'In_a_relationship'
						
			print(k.name + '  is in relationship with ' + l.name)
			log_maker(k.name + '  is in relationship with ' + l.name)
			break
