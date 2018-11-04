# -*- coding: utf-8 -*-
import sys, random, math
def chomp(x):
	if x.endswith("\r\n"):
		return x[:-2]
	if x.endswith("\n"):
		return x[:-1]
	return x
#Dichiarazioni
Conte = 0
Di_Maio = 0
Salvini = 0
R0 = random.random()
R1 = random.random()
R2 = random.random()
R3 = random.random()
R4 = random.random()
R5 = random.random()
R6 = random.random()
R7 = random.random()
nomefile = sys.argv[1]
print nomefile
with open(nomefile) as fp:  
	line = fp.readlines()
	maxcount = len(line)
	cg = 0
	while cg < maxcount:
		codice = chomp(line[cg])
		if codice == "BUONGIORNO AMICI":
			R1 = line[cg+1]
			cg = int(cg+1)
		elif codice == "CIAO AMICI":
			print(R1)
		elif codice == "VICEPREMIER SALVINI":
			Salvini = Conte
		elif codice == "VICEPREMIER DI MAIO":
			Di_Maio = Conte
		elif codice == "GIORGETTI":
			Conte = Salvini + Di_Maio
		elif codice == "BORGHI":
			Conte = Salvini - Di_Maio
		elif codice == "BAGNAI":
			Conte = Salvini/Di_Maio
		elif codice == "FOA":
			Conte = Salvini**Di_Maio
		elif codice == "SIRI":
			Conte = (Di_Maio**2)-4*(Salvini*Conte)
			Conte = Conte*random.random()
		elif codice == "MANOVRA":
			Di_Maio = Salvini = input(">>>")
		elif codice == "DIBBA":
			Conte = Di_Maio*Salvini
		elif codice == "CASALEGGIO":
			print("True")
		elif codice == "MATTARELLA":
			if Conte > 0:
				pass
			else:
				cg = cg + 1
		elif codice == "VOTA":
			gc = int(line[cg+1])-1
		elif codice == "MORISI":
			Rad = 1/Di_Maio
			Conte = math.pow(Salvini,Rad)
		elif codice == "MINISTRO SALVINI":
			Conte = Salvini
		elif codice == "MINISTRO DI MAIO":
			Conte = Di_Maio
		elif codice == "CASALINO":
			print("%s (Conte)"%Conte)
		elif codice == "POPULISTA":
			print("%s (Salvini)"%Salvini)
		elif codice == "BLOG":
			print("%s (Di Maio)"%Di_Maio)
		else:
			print("Line %s not executed"%int(cg+1))
		cg = cg + 1