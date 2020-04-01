greek=['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω','ά','έ','ή','ί','ό','ύ','ϊ','ϋ','ΐ','ΰ','ς','ώ'];
english = ['a','b','g','d','e','z','h','th','i','k','l','m','n','ks','o','p','r','s','t','y','f','x','ps','o','a','e','h','i','o','y','i','y','i','y','s','w']
o = open('ousiastika.txt','r',encoding='utf-8')
e = open('epitheta.txt','r',encoding='utf-8')
ow = open('ousiastika_greeklish.txt','w',encoding='utf-8')
ew = open('epitheta_greeklish.txt','w',encoding='utf-8')
for line in o.read().split():
	newline = line
	for letter in line:
		if letter in greek:
			newline = newline.replace(letter,english[greek.index(letter)])

	ow.write(newline+'\n')

for line in e.read().split():
	newline = line
	for letter in line:
		if letter in greek:
			newline = newline.replace(letter,english[greek.index(letter)])

	ew.write(newline+'\n')