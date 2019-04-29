import pickle

ecto = pickle.load(open('chem_dict.p', 'rb'))
pheno = pickly.load(open('pheno_dict.p', 'rb'))

data = ['Biobide_morph_4dpf_AC50.csv','Lein_morph_5dpf_AC50.csv','Tanguay_morph_5dpf_AC50.csv']

out_file = open('upload_data.csv', 'w')
out_file.write('chebi,ecto,phenotype,receptor,exposure,source,concentration,frequency,duration\n')

#conc = 'http://www.bioassayontology.org/bao#BAO_0000186'
receptor = 'http://purl.obolibrary.org/obo/NCBITaxon_7955'

counter = 0
for file in data:
	print(file)
	in_file = open(file, 'r')
	next(in_file)
	for line in in_file:
		line = line.strip('\n')
		row = line.split(',')
		ect,che = ecto[row[0]].split('|')
		frequency = 'acute'
		if ect == '':
			continue
		del row[0]
		if file == 'Biobide_morph_4dpf_AC50.csv':
			source = 'Biobide'
			conc = 'AC50'
			duration = '4d'
			for i,k in enumerate(row):
				if k != '' and i != 15:
					p = pheno_dict[i]
					phen = p.split('\t')
					phenotype = phen[1]
					exposure = 'EXP_' + str(counter)
					output = [che,ect,phenotype,receptor,exposure,source,conc,frequency,duration]
					out_file.write(','.join(output) + '\n')
					counter = counter + 1
				else:
					continue
		elif file == 'Lein_morph_5dpf_AC50.csv':
			source = 'Lein'
			conc = 'AC50'
			duration = '5d'
			for i,k in enumerate(row):
				if k != '':
					if i == 16:
						continue
					else:
						p = pheno_dict[i]
						phen = p.split('\t')
						phenotype = phen[1]
						exposure = 'EXP_' + str(counter)
						output = [che,ect,phenotype,receptor,exposure,source,conc,frequency,duration]
						out_file.write(','.join(output) + '\n')
						counter = counter + 1
				else:
					continue
		elif file == 'Tanguay_morph_5dpf_AC50.csv':
			source = 'Tanguay'
			conc = 'AC50'
			duration = '5d'
			for i,k in enumerate(row):
				if k != '':
					if i == 16:
						continue
					else:
						p = pheno_dict[i]
						phen = p.split('\t')
						phenotype = phen[1]
						exposure = 'EXP_' + str(counter)
						output = [che,ect,phenotype,receptor,exposure,source,conc,frequency,duration]
						out_file.write(','.join(output) + '\n')
						counter = counter + 1
				else:
					continue
		else:
			print('error')