#impoter la bibliteque mysql.connector
import mysql.connector as mysql
import datetime
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

try:
    #connexion à la base de données 'data'
    cnx = mysql.connect(
        user= USER,
        password= PASSWORD,
        database= DATABASE
        )
    
    cursor = cnx.cursor()
    
    #créé la d^base de données 'data'
    query ="""CREATE DATABASE IF NOT EXISTS `data`;
                USE `data`;
                CREATE TABLE IF NOT EXISTS `data_temp_hum` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `temperature` FLOAT NOT NULL,
                    `humidite` FLOAT NOT NULL,
                    `date` DATETIME NOT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;"""
                
    cursor.execute(query)
    
    #recuper la date du jour format AAAA-MM-JJ + heure
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #remplir la table 'data_temp_hum' avec des valeurs aléatoires
    values = (cursor.lastrowid, randint(-100,100), randint(0,100), date)
    
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
