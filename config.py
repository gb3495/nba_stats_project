import mysql.connector
import MySQLdb
from MySQLdb import _mysql
from mysql.connector import connect, errorcode
import json
import requests
import pandas as pd

#   Method to establish and verify connection to server

def connectToServer():
    try:
        db = MySQLdb.connect("127.0.0.1", "root", "butler445", "final_project")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
            print("Connection established") 


