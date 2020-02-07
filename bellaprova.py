# Programma genera e salva password e per cosa è stato utilizzato
import random
possibili_caratteri = ''
numero_caratteri = ''
password = ''
# Richiedi se vuole lettere minuscole
def richiesta_lettere_minuscole() :

	scelta_password = ''
	print('''Vuoi le lettere minuscole? [si/no]''')
	scelta_password = str(input())
	
	while((scelta_password != 'si') and (scelta_password != 'no') and (scelta_password != 'sì')):
		
		print('Errore')
		print('''Vuoi le lettere minuscole? [si/no]''')
		scelta_password = str(input())
	return scelta_password

# Richiedi se vuole lettere maiuscole
def richiesta_lettere_maiuscole() :

	scelta_password = ''
	print('''Vuoi le lettere maiuscole? [si/no]''')
	scelta_password = str(input())
	
	while((scelta_password != 'si') and (scelta_password != 'no') and (scelta_password != 'sì')):
		
		print('Errore')
		print('''Vuoi le lettere maiuscole? [si/no]''')
		scelta_password = str(input())
	return scelta_password

# Richiedi se vuole numeri
def richiesta_numeri() :

	scelta_password = ''
	print('''Vuoi i numeri? [si/no]''')
	scelta_password = str(input())
	
	while((scelta_password != 'si') and (scelta_password != 'no') and (scelta_password != 'sì')):
		
		print('Errore')
		print('''Vuoi i numeri? [si/no]''')
		scelta_password = str(input())
	return scelta_password

# Richiedi se vuole i caratteri ascii
def richiesta_ascii() :

	scelta_password = ''
	print('''Vuoi i caratteri ascii? [si/no]''')
	scelta_password = str(input())
	
	while((scelta_password != 'si') and (scelta_password != 'no') and (scelta_password != 'sì')):
		
		print('Errore')
		print('''Vuoi i caratteri ascii? [si/no]''')
		scelta_password = str(input())
	return scelta_password

stringa_lettere_maiuscole = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
stringa_lettere_minuscole = 'abcdefghijklmnopqrstuvwxyz'
stringa_numeri = '0987654321'
stringa_ascii = " !#£$%&()*+-/:;=<>?@"

# Richiesta e controllo lunghezza password
while(numero_caratteri == ''):
	numero_caratteri = int(input('Inserisci la lunghezza della password (devono essere almeno 5 caratteri): '))
	if(numero_caratteri < 4):
		print('Password troppo corta:')
		numero_caratteri = ''

	if(numero_caratteri > 10000):
		print('Password troppo lunga:')
		numero_caratteri = ''


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

print(password)

input sito per la passwoed

word inserisco password e sito in tabella
		


