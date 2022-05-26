#impoter la bibliteque mysql.connector
import datetime
from random import randint
import mysql.connector as mysql

try:
    #connexion à la base de données 'data'
    cnx = mysql.connect(user='ccln', password='1234', host='localhost', database='data')
    cursor = cnx.cursor()
    
    values = (cursor.lastrowid, randint(-100,100), randint(0,100), datetime.date.today())

    #requete sql
    sql = "INSERT INTO `data_temp_hum` (`id`, `temperature`, `humidite`, `date`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, values)
    cnx.commit()
  
    #affichage de la requete
    print(cursor.rowcount, "record inserted.")

    #une requete req qui affiche toutes les données de la table
    req = "SELECT * FROM `data_temp_hum`"
    cursor.execute(req)
    for (id, temperature, humidite, date) in cursor:
        print("id = ", id, "temperature = ", temperature, "humidite = ", humidite, "date = ", date)

except mysql.Error as err:
    print("Something went wrong: {}".format(err))

finally:
    cnx.close()