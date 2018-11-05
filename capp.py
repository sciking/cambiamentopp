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
	whereis = 0
	while whereis < maxcount:
		codice = chomp(line[whereis])
		if codice == "ONOREVOLI COLLEGHI":
			cg = whereis
			inizio = whereis
			break
		else:
			pass
with open(nomefile) as fp:  
	line = fp.readlines()
	maxcount = len(line)
	cg = 0
	while cg < maxcount:
		codice = chomp(line[cg])
		if codice == "DISCUTIAMO IL DDL":
			print("Blocco logico: %s",chomp(line[cg+1]))
			cg = cg+1
		if codice == "CONTRATTO":
			Var1 = Salvini 
			Var2 = Di_Maio 
			Salvini = Var2
			Di_Maio  = Var1
		if codice == "LA CAMERA APPROVA":
			exit()
		if codice == "LA CAMERA RESPINGE":
			cg = inizio
		if codice == "BUONGIORNO AMICI":
			R1 = chomp(line[cg+1])
			cg = int(cg+1)
		elif codice == "CIAO AMICI":
			print(R1)
		elif codice == "VICEPREMIER SALVINI":
			Salvini = Conte
		elif codice == "VICEPREMIER DI MAIO":
			Di_Maio = Conte
		elif codice == "LA GENTE È STANCA":
			Conte = Salvini + Di_Maio
		elif codice == "L'ONESTÀ ANDRÀ DI MODA":
			Conte = Salvini - Di_Maio
		elif codice == "BRUXELLES NON CI SPAVENTA":
			Conte = Salvini/Di_Maio
		elif codice == "REDDITO DI CITTADINANZA":
			Conte = Salvini**Di_Maio
		elif codice == "I MERCATI SE NE FARANNO UNA RAGIONE":
			Conte = (Di_Maio**2)-4*(Salvini*Conte)
			Conte = Conte*random.random()
		elif codice == "BISOGNA PENSARE ALLA TRASPARENZA":
			Conte = Di_Maio*Salvini
		elif codice == "CASALEGGIO":
			print("True")
		elif codice == "MATTARELLA FIRMA IL DECRETO":
			if Conte > 0:
				pass
			else:
				cg = cg + 1
		elif codice == "VOTIAMO IL PROGETTO DI LEGGE":
			gc = int(line[cg+1])-1
		elif codice == "PRIMA GLI ITALIANI":
			Rad = 1/Di_Maio
			Conte = math.pow(Salvini,Rad)
		elif codice == "MINISTRO SALVINI":
			Conte = Salvini
		elif codice == "MINISTRO DI MAIO":
			Conte = Di_Maio
		elif codice == "IL POPOLO CHIEDE SALVINI":
			Salvini = float(input("(Salvini)>>>"))
		elif codice == "IL POPOLO CHIEDE DI MAIO":
			Di_Maio = float(input("(Di Maio)>>>"))
		elif codice == "IL POPOLO CHIEDE CONTE":
			Conte = float(input("(Conte)>>>"))
		elif codice == "SALVINI, LO VUOLE L'ITALIA":
			print("%s (Salvini)"%Salvini)
		elif codice == "DI MAIO, LO VUOLE L'ITALIA":
			print("%s (Di Maio)"%Di_Maio)
		elif codice == "CONTE, LO VUOLE L'ITALIA":
			print("%s (Conte)"%Conte)
		elif codice == "IL PRESIDENTE DEL CONSIGLIO":
			Conte = Conte/2
		elif codice == "NON È NEL CONTRATTO":
			Conte = 1/Conte
		elif codice == "ABBIAMO SALVATO VITE":
			Conte = Conte*2
		elif codice == "L'AVVOCATO DEL POPOLO":
			Conte = Conte*10
		elif codice == "METTEREMO LA FIDUCIA":
			Conte = Conte**Conte
		else:
			print("Line %s not executed"%int(cg+1))
		cg = cg + 1