import threading 
import socket
import mysql.connector
import smtplib_mail
PASSWORD_CORRETTA="marani1234"
comunicazioni = ["",""]
db_lock=threading.Lock()
db_conn = mysql.connector.connect(
        host="10.10.0.10",
        user="riccardo_marani",
        password="marani1234",
        database="5ATepsit",
        port=3306, 
        )


def gestisci_comunicazione(conn):
    conn.send("Benvenuto, inserisci la password: ".encode())
    data = conn.recv(1024).decode()
    tentativi=0
    while data != PASSWORD_CORRETTA and tentativi<2:
        tentativi+=1
        conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {2-tentativi} ".encode())
        data = conn.recv(1024).decode()      

    if(data != PASSWORD_CORRETTA):
        conn.send("STOP".encode())
        conn.close()
        return

    while True:
        conn.send("Benvenuto, cosa vuoi fare: I=insert, U=update,S=read,D=delete".encode())
        data = conn.recv(1024).decode()
        print(data)
        if(data=="I"):
            conn.send("su che tabella vuoi inserire: C=clienti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode()            
            dati_query = db_insert(data,conn)
            print(dati_query)
        elif(data=="S"):
            ritorno=db_select(conn)
            print(ritorno)
        elif(data=="U"):
            db_update(conn)
        elif(data=="D"):
            conn.send("su che tabella vuoi eliminare: C=clienti, Z=zone di lavoro".encode())
            data = str(conn.recv(1024).decode()) 
            #passaggio dati         
            #   
            dati_query = db_delete(data,conn)
            print(dati_query) 
        

##################################################################################################################################
def db_insert(data,conn):
    cur = db_conn.cursor()
    if(data=="C"):
        with db_lock:
            conn.send("inserisci ID dipendente: ".encode())
            id_dipendente=str(conn.recv(1024).decode())
            conn.send("inserisci nome dipendente: ".encode())
            nome=str(conn.recv(1024).decode())
            conn.send("inserisci cognome: ".encode())
            cognome=str(conn.recv(1024).decode())
            conn.send("inserisci indirizzo: ".encode())
            indirizzo=str(conn.recv(1024).decode())
            conn.send("inserisci pos_lav: ".encode())
            posizione_lavorativa=str(conn.recv(1024).decode())
            conn.send("inserisci data assunzione(anno-mese-g): ".encode())
            data_assunzione=str(conn.recv(1024).decode())
            conn.send("inserisci data nascita(anno-mese-g): ".encode())
            data_nascita=str(conn.recv(1024).decode())
            query = f"INSERT INTO `dipendenti_riccardo_marani`(`id_dipendente`, `nome`, `cognome`, `indirizzo`, `posizione_lavorativa`, `data_assunzione`, `data_nascita`) VALUES ('%s','%s','s%','s%','s%','s%','s%')"
            values=(id_dipendente, nome, cognome, indirizzo, posizione_lavorativa, data_assunzione, data_assunzione, data_nascita)
            cur.execute(query, values)
            db_conn.commit()
    elif(data=="Z"):
        with db_lock:
            conn.send("inserisci ID dipendente: ".encode())
            id_zona=str(conn.recv(1024).decode())
            conn.send("inserisci nome dipendente: ".encode())
            nome_zona=str(conn.recv(1024).decode())
            conn.send("inserisci cognome: ".encode())
            numero_clienti=str(conn.recv(1024).decode())
            conn.send("inserisci indirizzo: ".encode())
            id_dipendente=str(conn.recv(1024).decode())
            conn.send("inserisci pos_lav: ".encode())
            ore_di_lavoro_giornaliere=str(conn.recv(1024).decode())
            query = f"INSERT INTO `zona_di_lavoro_marani_riccardo`(`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendente`, `ore_di_lavoro_giornaliere`) VALUES ('%s','%s','%s','','{ore_di_lavoro_giornaliere}')"
            values=(id_zona, nome_zona,numero_clienti,id_dipendente,ore_di_lavoro_giornaliere)
            cur.execute(query,values)
            db_conn.commit()

    return "dati inseriti correttamente"
################################################################################################################################
def db_select(conn):  

    conn.send("dove vuoi cercare (clienti, o zona)?".encode())
    tab=conn.recv(1024).decode()
    if tab=="C":
        query = "SELECT * FROM dipendenti_riccardo_marani"
    else:
        query = "SELECT * FROM zona_di_lavoro_marani_riccardo"
    cur = db_conn.cursor() 
    cur.execute(query)
    dati = cur.fetchall()

    return dati
#################################################################################################################################
def db_update(conn):
    with db_lock:
        cur = db_conn.cursor()
        conn.send("inserisci tabella")
        tabella=conn.recv(1024).decode()
        conn.send("inserisci valore da modificare: ".encode())
        valore=conn.recv(1024).decode()
        conn.send("inserisci parametro: ".encode())
        parametro=conn.recv(1024).decode()
        conn.send("inserisci valore nuovo da cambiare: ".encode())
        nuovo=conn.recv(1024).decode()

        query= "UPDATE "+ tabella + " SET " + parametro + "=\'" + valore + "\' WHERE" +parametro + "=\'" +nuovo+ "\'"

        cur=db_conn.cursor()
        cur.execute(query)
        db_conn.commit()



#############################################################################################################################################
def db_delete(data, conn):
    with db_lock:
        cur = db_conn.cursor()
        conn.send("inserisci tipo di parametro da cambiare: ".encode())
        tipo=str(conn.recv(1024).decode())
        conn.send("inserisci valore da cambiare: ".encode())
        valore=str(conn.recv(1024).decode())
        if data=="C":
            data="dipendenti_riccardo_marani"
        else:
            data="zone_di_lavoro_riccardo_marani"

        # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
        query = f"DELETE FROM "+ data + " where " + tipo + " =\'" + valore + "\'"
        print(query)
        cur.execute(query)
        db_conn.commit()
        smtplib_mail.invio()

        return "eliminato correttamente"

##################################################################################################################################
print("server in ascolto: ")
lock = threading.Lock()
HOST = ''                 # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50010            # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i=0

while True:
    lista_connessioni.append( s.accept() ) #connessione = s.accept() 
    print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) )) 
    thread[i].start()
    i+=1