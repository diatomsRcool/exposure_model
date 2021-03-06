import pickle

in_file = open('phenotype_map.txt','r')

pheno_dict = {}

next(in_file)
for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	pheno = row[0]
	zp = row[1]
	label = row[2]
	pheno_dict[pheno] = label + '|' + zp
	
pickle.dump(pheno_dict, open('pheno_dict.p', 'wb'))