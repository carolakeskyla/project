#sys - võtame vastu süsteemi poolt antud sisendit
#argv - sisendilist nt. [sisendArv1, sisendArv2]
from sys import argv

#väärtustame sisendid (py <script> a b)
script, a, b = argv

#sisendina saame String tüüpi väärtused 
a = int(a)
b = int(b)


#defineerime lihtsa liitmisfunktsiooni 
def fun(a, b):
	print(a+b)

#kutsume funktsiooni välja 
fun(a, b)