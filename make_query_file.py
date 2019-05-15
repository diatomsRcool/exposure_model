import pickle

chem = pickle.load(open('chem_dict.p', 'rb'))
pheno = pickle.load(open('pheno_dict.p', 'rb'))

lab_data = open('all_data.txt', 'r')

out_file = open('query_data.txt', 'w')
out_file.write('cas	phenotype	source	concentration	duration	phenotype_label	phenotype_CURIE	chem_label	chem_curie\n')

next(lab_data)
for line in lab_data:
	line = line.strip('\n')
	row = line.split('\t')
	source = row[2]
	duration = row[4]
	conc = row[3]
	cas = row[0]
	phen = row[1]
	chem_ecto, chem_curie, chem_label = chem[cas].split('|')
	pheno_label, pheno_curie = pheno[phen].split('|')
	out_file.write('\t'.join([cas,phen,source,conc,duration,pheno_label,pheno_curie,chem_label,chem_curie]) + '\n')