import pickle

ecto = pickle.load(open('chem_dict.p', 'rb'))

data = ['Biobide_morph_4dpf_AC50.csv','Lein_morph_5dpf_AC50.csv','Tanguay_morph_5dpf_AC50.csv']

out_file = open('upload_data.tsv', 'w')
out_file.write('stimulus	phenotype	receptor	exposure	source\n')

#conc = 'http://www.bioassayontology.org/bao#BAO_0000186'
receptor = 'http://purl.obolibrary.org/obo/NCBITaxon_7955'

biobide_dict = {
0:'Mortality	http://purl.obolibrary.org/obo/UBERON_0000071',
1:'Jaw morphology	http://purl.obolibrary.org/obo/ZP_0009598',
2:'Microcephaly or abnormal head shape	http://purl.obolibrary.org/obo/ZP_0002314',
3:'Microphthalmia/Cyclopia	http://purl.obolibrary.org/obo/ZP_0000043',
4:'Head edema	http://purl.obolibrary.org/obo/ZP_0001451',
5:'Malformation of the sacculi/otoliths	http://purl.obolibrary.org/obo/ZP_0001920',
6:'Heart edema/irregular shape	http://purl.obolibrary.org/obo/ZP_0005892',
7:'Abnormal heartbeat	http://purl.obolibrary.org/obo/ZP_0012799',
8:'Length alteration	http://purl.obolibrary.org/obo/ZP_0012799',
9:'Curved/curled	http://purl.obolibrary.org/obo/ZP_0002347',
10:'Notochord morphology	http://purl.obolibrary.org/obo/ZP_0000624',
11:'Malformation of the tail (including tail fins)	http://purl.obolibrary.org/obo/ZP_0004969',
12:'Yolk edema	http://purl.obolibrary.org/obo/ZP_0010821',
13:'Yolk opacity	http://purl.obolibrary.org/obo/ZP_0002198',
14:'Somite morphology	http://purl.obolibrary.org/obo/ZP_0000011',
15:'Other effects	',
16:'Hatching	http://purl.obolibrary.org/obo/ZP_0003211',
17:'Necrotic tissues	http://purl.obolibrary.org/obo/ZP_0000398'
}

lein_dict = {
0:'Mortality	http://purl.obolibrary.org/obo/UBERON_0000071',
1:'Halted Dev.	http://purl.obolibrary.org/obo/ZP_0000305',
2:'Craniofacial	http://purl.obolibrary.org/obo/ZP_0001609',
3:'Yolk E.	http://purl.obolibrary.org/obo/ZP_0000102',
4:'Par E.	http://purl.obolibrary.org/obo/ZP_0001241',
5:'Red heart	http://purl.obolibrary.org/obo/ZP_0005930',
6:'Axis	http://purl.obolibrary.org/obo/ZP_0005012',
7:'Notochord	http://purl.obolibrary.org/obo/ZP_0000627',
8:'C. Fin	http://purl.obolibrary.org/obo/ZP_0010405',
9:'Pectoral Fin	http://purl.obolibrary.org/obo/ZP_0000055'
}

tanguay_dict = {
0:'MORT	http://purl.obolibrary.org/obo/UBERON_0000071',
1:'YSE_	http://purl.obolibrary.org/obo/ZP_0000102',
2:'AXIS	http://purl.obolibrary.org/obo/ZP_0005012',
3:'EYE_	http://purl.obolibrary.org/obo/ZP_0008271',
4:'SNOU	http://purl.obolibrary.org/obo/ZP_0014550',
5:'JAW_	http://purl.obolibrary.org/obo/ZP_0009598',
6:'OTIC	http://purl.obolibrary.org/obo/ZP_0001601',
7:'PE__	http://purl.obolibrary.org/obo/ZP_0009266',
8:'BRAI	http://purl.obolibrary.org/obo/ZP_0000100',
9:'SOMI	http://purl.obolibrary.org/obo/ZP_0000011',
10:'PFIN	http://purl.obolibrary.org/obo/ZP_0000055',
11:'CFIN	http://purl.obolibrary.org/obo/ZP_0010405',
12:'PIG_	http://purl.obolibrary.org/obo/ZP_0022396',
13:'CIRC	http://purl.obolibrary.org/obo/ZP_0001225',
14:'TRUN	http://purl.obolibrary.org/obo/ZP_0003437',
15:'SWIM	http://purl.obolibrary.org/obo/ZP_0020238',
16:'NC__	http://purl.obolibrary.org/obo/ZP_0000624',
17:'TR__	http://purl.obolibrary.org/obo/ZP_0000624'
}

counter = 0
for file in data:
	print(file)
	in_file = open(file, 'r')
	next(in_file)
	for line in in_file:
		line = line.strip('\n')
		row = line.split(',')
		stimulus = ecto[row[0]]
		if stimulus == '':
			continue
		del row[0]
		if file == 'Biobide_morph_4dpf_AC50.csv':
			source = 'Biobide'
			for i,k in enumerate(row):
				if k != '' and i != 15:
					p = biobide_dict[i]
					phen = p.split('\t')
					phenotype = phen[1]
					exposure = 'EXP_' + str(counter)
					output = [stimulus,phenotype,receptor,exposure,source]
					out_file.write(','.join(output) + '\n')
					counter = counter + 1
				else:
					continue
		elif file == 'Lein_morph_5dpf_AC50.csv':
			source = 'Lein'
			for i,k in enumerate(row):
				if k != '':
					if i == 16:
						continue
					else:
						p = lein_dict[i]
						phen = p.split('\t')
						phenotype = phen[1]
						exposure = 'EXP_' + str(counter)
						output = [stimulus,phenotype,receptor,exposure,source]
						out_file.write(','.join(output) + '\n')
						counter = counter + 1
				else:
					continue
		elif file == 'Tanguay_morph_5dpf_AC50.csv':
			source = 'Tanguay'
			for i,k in enumerate(row):
				if k != '':
					if i == 16:
						continue
					else:
						p = tanguay_dict[i]
						phen = p.split('\t')
						phenotype = phen[1]
						exposure = 'EXP_' + str(counter)
						output = [stimulus,phenotype,receptor,exposure,source]
						out_file.write(','.join(output) + '\n')
						counter = counter + 1
				else:
					continue
		else:
			print('error')