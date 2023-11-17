import socket

HOST = 'localhost'
PORT = 50010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    if(data.decode()=="STOP"):
        print("password ERRATA troppe volte, disconnessione server")
        break
    print('Received: ', data.decode())
    testo = input("").encode()
    s.send(testo)

s.close()
'''In questo codice, ho aggiunto il conteggio dei tentativi per la password nel server. Se il client inserisce la password errata per tre volte, il server chiude la connessione. 
Se il client inserisce la password corretta, il server consente all'utente di selezionare l'azione da eseguire (in questo caso, "R" per la query SELECT * dal database).
Assicurati di aver configurato correttamente la connessione al database e sostituisci "PASSWORD_CORRETTA" con la tua password effettiva.'''




