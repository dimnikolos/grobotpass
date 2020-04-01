f = open('lexeis.txt','r',encoding='utf-8')
o = open('ousiastika.txt','w',encoding='utf-8')
e = open('epitheta.txt','w',encoding='utf-8')
for line in f.read().split():
	x = None
	while x not in ['Ο','Η','ΤΟ','ΟΙ','ΤΑ','Ε','Χ']:
		print(line)
		x = input("Ο/Η/Τ ή Ε για επίθετο ή Χ για παράβλεψη>")
		if x != 'Χ':
			if x in ['Ο','Η','ΤΟ','ΟΙ','ΤΑ']:
				o.write(','.join([x,line])+'\n')
			else:
				e.write(line)
