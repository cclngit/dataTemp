import datetime
import Adafruit_DHT
import mysql.connector as mysql
from random import randint
from time import sleep
from sys import exit

#instansition capteur DHT11
pin = 4
dht = Adafruit_DHT.DHT11 #type de capteur DHT11 mettre DHT11 ou DHT22

while True:
    try:
        #connexion à la base de données 'data'
        cnx = mysql.connect(user='....',        #user
                        password='****',        #password
                        port = 0000,            #port par défaut
                        host='XXX.XXX.XXX.XXX', #adresse IP du serveur
                        database='YYYYY'        #nom de la base de données
                        )
    
        #cré un curseur
        cursor = cnx.cursor()
        
        #Lecture des données temp et hum
        humidite, temperature = Adafruit_DHT.read_retry(dht, pin)
        
    except mysql.Error as err:
        print("Une erreur s'est produite : {}".format(err))
        
    finally:
        #recuper la date du jour format AAAA-MM-JJ + heure
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Remplissage de la base de donnée format id | temp | hum | date + heure
        donnees = (cursor.lastrowid, temperature, humidite, date)

        #requete sql INSERT INTO `nom_de_la_table` (`format`, `de`, `donnees`, `...`) VALUES (%s, %s, %s, %s,...)
        requete = "INSERT INTO `data_temp_hum` (`id`, `temperature`, `humidite`, `date`) VALUES (%s, %s, %s, %s)"
        
        #execution de la requete
        cursor.execute(requete, donnees)

        #commit pour enregistré les données
        cnx.commit()
        
        #attendre 30 min "sleep(1800)" pour la prochaine lecture (ici 2 secondes pour tester)
        sleep(2)
