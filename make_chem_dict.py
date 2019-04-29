import pickle

in_file = open('CAS_map.txt','r')

chem_dict = {}

next(in_file)
for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	CAS = row[0]
	exp = row[3]
	chebi = row[1]
	print(CAS)
	print(exp)
	chem_dict[CAS] = exp + '|' + chebi
	
pickle.dump(chem_dict, open('chem_dict.p', 'wb'))