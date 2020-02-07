#Programma che preleva una password casuale e la inserisce in una tabella su word con due colonne una per la pswd e una per il sito 
from docx import Document
from docx.shared import Cm
import random
from funzioni_programma import richiesta_lettere_minuscole
from funzioni_programma import richiesta_lettere_maiuscole
from funzioni_programma import richiesta_numeri
from funzioni_programma import richiesta_ascii
from funzioni_programma import richiesta_lunghezza_psw
import xlrd
import xlwt

# Programma genera e salva password
possibili_caratteri = ''
numero_caratteri = ''
password = ''
utilizzo = ''

while(utilizzo == ''):
	utilizzo = str(input('Vuoi leggere una password? [si/no] '))
	if(utilizzo == 'si'):
		# Apre il file Excel
		book = xlrd.open_workbook('C:/Users/Misure/Desktop/Python/Archiviatore_password.xlsx')
		# Così si sceglie su quale foglio lavorare
		sheet = book.sheet_by_index(0)

		sito = str(input('Di che sito è la password che stai cercando?'))
		for row_num in range(sheet.nrows):
			row_value = sheet.row_values(row_num)
			if row_value[0] == sito:
				print('Sito:        Password:')
				print(row_value)

	elif(utilizzo == 'no'):
		utilizzo = str(input('Vuoi inserire una nuova password? [si/no] '))
		if( utilizzo == 'si'):
			stringa_lettere_maiuscole = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			stringa_lettere_minuscole = 'abcdefghijklmnopqrstuvwxyz'
			stringa_numeri = '0987654321'
			stringa_ascii = "!#£$%&()*+-/:;=<>?@"

			# Richiesta e controllo lunghezza password
			numero_caratteri = richiesta_lunghezza_psw(numero_caratteri)

			# Se selezionato aggiunta lettere minuscole ai caratteri da usare nella password
			if((richiesta_lettere_minuscole()) != 'no'):
				possibili_caratteri = possibili_caratteri + stringa_lettere_minuscole
				# Aggiunge a password almeno una lettera minuscola se sono volute nella password
				password = password + (random.choice(stringa_lettere_minuscole))
				numero_caratteri = numero_caratteri - 1

			# Se selezionato aggiunta lettere maiuscole ai caratteri da usare nella password
			if((richiesta_lettere_maiuscole()) != 'no'):
				possibili_caratteri = possibili_caratteri + stringa_lettere_maiuscole
				# Aggiunge a password almeno una lettera maiuscola se sono volute nella password
				password = password + (random.choice(stringa_lettere_maiuscole))
				numero_caratteri = numero_caratteri - 1

			# Se selezionato aggiunta numeri ai caratteri da usare nella password
			if((richiesta_numeri()) != 'no'):
				possibili_caratteri = possibili_caratteri + stringa_numeri
				# Aggiunge a password almeno un numero se sono voluti nella password
				password = password + (random.choice(stringa_numeri))
				numero_caratteri = numero_caratteri - 1

			# Se selezionato aggiunta caratteri ascii ai caratteri da usare nella password
			if((richiesta_ascii()) != 'no'):
				possibili_caratteri = possibili_caratteri + stringa_ascii
				# Aggiunge a password almeno un carattere ascii se sono voluti nella password
				password = password + (random.choice(stringa_ascii))
				numero_caratteri = numero_caratteri - 1

			# Generazione password
			for x in range(numero_caratteri):
				password = password + (random.choice(possibili_caratteri))

			# Rimescolamento password
			password = ''.join(random.sample(password,len(password)))
			print('La tua password è: ')
			print(password)

			nuovo_sito = ''
			nuovo_sito = str(input('Inserisci il nome del nuovo sito a cui vuoi collegare la Password: '))
			book = xlrd.open_workbook('C:/Users/Misure/Desktop/Python/Archiviatore_password.xlsx')
			sheet = book.sheet_by_index(0)
			for row_num in range(sheet.nrows):
				row_value = sheet.row_values(row_num)
				if row_value[0] == '':
					row_value[0] = sito
					row_value [1] = password
			#book.save("C:/Users/Misure/Desktop/Python/Archiviatore_password.xlsx")

