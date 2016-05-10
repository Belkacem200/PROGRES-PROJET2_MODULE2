import socket #Bibliothecque socket
import time #bibliothecque de temps (pour regarder la date des connexion aux liens par les employes
import sys #appelee pour sortir du programme 'exit'
import re #regular expression
import urllib3 #Pour la recuperation des get 
from threading import * #Pour le threading des socket
import glob #utilisee pour la suppression des fichier html de toutes extension
import os #utilisee pour la suppression des fichier html 

#Suppression des fichier contenant les liens visites par les clients existant dans le cache 'pour relandcer le proxy'
#_________________________________________________________#
directory='../config/html/'
os.chdir(directory)
files=glob.glob('*')
for filename in files:
    os.unlink(filename)
os.chdir('../../proxy/') #Pour revenir au directory courant
#_________________________________________________________#

compteur = 1
LOCK = Lock()

#Fonction d ecriture sur le fichier en sortie
def writeInFile(compteur, time, date, address, html):
    outputfile = open("../config/html/" + str(compteur), 'w') #Definition du directory d'administration
    outputfile.write(str(compteur) + "\n" + time + "\n" + date + "\n" + address + "\n" + html + "\n") #Formattage de l'ecriture sur le fichier 'INSPECTION'
    return

#Fonction gerant le temps et la reception des donnees
def recv_timeout(the_socket, timeout=2):
    global compteur
    the_socket.setblocking(0)

    total_data = [] #liste des  donnees
    data = '' #la donnee

    begin = time.time()
    while 1:
        if total_data and time.time()-begin > timeout: #Verification de la validite du TTL de la requete
            break

        elif time.time()-begin > timeout*2:
            break

        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data.decode())
                begin = time.time() #Pour ecrire le temps dans le fichier en sortie pour l afficher sur l'interface Inspection
            else:
                time.sleep(0.1) #Pour gerer le temps de reponse du serveur 'qui depend de la distance'
        except:
            pass

    return ''.join(total_data) #Retour des donnees 

#Fonction d'envoie de la requete cliente au serveur
def envoyer_au_serveur(url, request):
    global compteur
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return r.data

#Fonction de recuperation de la requete GET du client 'employe'
def handle_client(socket_client, address_client):
    global compteur
    Donnee_client = socket_client.recv(90000).decode() #reception de la socket du client
    print("#ADDRESS_CLIENT: ", address_client)
    if not Donnee_client: #si le client n'envoie rien on ferme la connexion
        socket_client.close()
        sys.exit()

    reg_http = re.compile(r'GET (http://[a-z0-9]+\.[^.]*\.[a-z]*)/', re.IGNORECASE) #expression reguliere recuperant le lien http demande par le client
    url = Donnee_client.split(' ')[0] + ' ' + Donnee_client.split(' ')[1] + '\n'
    m = reg_http.search(url)
    if m:
        url = m.group(1) + '\n'  #affectation de l'url concatenee avec un retour a la ligne
    else: #aucun lien ne match 
        print("L'expression reguliere ne match pas avec le lien: ", 'http://' + url)
        socket_client.close()
        return

    allowed = False #initialisation

    fd = open("../config/whitelist/whitelist.txt", "r+")
    for i in fd:
        if url == i: #si l'url demande par le client est authorise par l'admin
            allowed = True #site web austorise

    if not allowed:
        print('$$$$$URL NOT ALLOWED: ', Donnee_client.split(' ')[1])
        socket_client.sendall('HTTP/1.0 404 Not Found\nContent-Type: text/html\n\n       <h1> YOU ARE NOT ATHORISED TO ACCESS THIS WEBSITE </h1> \n\n Please Contact your Admin to get more informations'.encode())
        print(Donnee_client)

    else: #si authorise ==> Gestion de la section critique
		#compteur est une section critique
        LOCK.acquire() #Verification de possession du verrou sinon attente
        writeInFile(compteur, time.strftime("%H:%M:%S"), time.strftime("%d/%m/%Y"), address_client[0], Donnee_client.split(' ')[1])
        compteur += 1
        LOCK.release() #liberation du verrou

        print('#URL ALLOWED: ', Donnee_client.split(' ')[1]) #affichage de l'envoie du client
        answer = envoyer_au_serveur(Donnee_client.split(' ')[1], Donnee_client) #envoyer les donnees du client au serveur
        socket_client.sendall(answer)

    socket_client.close()#fermeture socket cliente
    return


hostProxy = ''
portProxy = 6060 #Proxy d'administration

sock_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_temp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_temp.bind((hostProxy, portProxy))
sock_temp.listen(80) #port d'ecoute

while 1:
    socket_client, address_client = sock_temp.accept()
    Thread(target=handle_client, args=(socket_client, address_client,)).start() #thread servant a gerer plusieurs connexions
