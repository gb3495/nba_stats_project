#   Owner: Griffin Butler
#   Name: CS 286 Final Project
#   Version: 1.2.1
#   Date: November 1st 2021
#   Organization: Worcester State University
#
#
#   The goal of this project is to connect a MySQL database to one or more python
#   scripts to analyze and evaluate statistics from prior seasons of NBA basketball
#   and to utilize this information to make educated and accurate predictions
#   on the performance of individual NBA teams.
#
#
#   The data has been retrieved from NBA.com, and is imported as a .csv file into MySQL.


#   Import statements
import numpy as np
import mysql.connector
import MySQLdb
from MySQLdb import _mysql
from mysql.connector import errorcode
import matplotlib.pyplot as plt
from numpy.lib.function_base import diff

from config import connectToServer


#   Establish connection to MySQL server
#   Test connection

class Connect():
    def connectToServer():
        try:
            db = MySQLdb.connect("127.0.0.1", "root", "butler445", "nba_stats")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("Connection established")

#   Recieves data from SQL stored procedure
#   Data is team win percentage from 2014-2016

class toArray():
    def getTrainingValues():
        db = MySQLdb.connect("127.0.0.1", "root", "butler445", "nba_stats")
        cursor = db.cursor()
        cursor.callproc('getTrainingValues')
        output = cursor.fetchall()
        arr = np.array(output)

        return arr

#   Recieves data from SQL stored procedure
#   Data is team win percentage in 2017

    def getTestValues():
        db = MySQLdb.connect("127.0.0.1", "root", "butler445", "nba_stats")
        cursor = db.cursor()
        cursor.callproc('getTestValues')
        output = cursor.fetchall()
        arr = np.array(output)

        return arr

#   Recieves data from SQL stored procedure
#   Data is team names

    def getTeamNames():
        db = MySQLdb.connect("127.0.0.1", "root", "butler445", "nba_stats")
        cursor = db.cursor()
        cursor.callproc('getTeams')
        output = cursor.fetchall()
        arr = np.array(output)

        return arr

#   Makes prediction based on a line of best fit
#   Uses data for seasons 1, 2, 3 to compute the slope
#   Applies slope to compute an estimate for season 4
#   Estimate is compared against actual win percentage

    def makePrediction():
        i = 0
        total = 0
        while i < 29:
            x = [1, 2, 3]
            y = trainingValues[i]
            m, b = np.polyfit(x, y, 1)

            print("----------------------------------------------")
            team = teamNames[i]
            print(team)
            print("Estimated win percentage:")
            print(m * 4 + b)
            val = (float)(testValues[i])
            print("Actual 2017-2018 win percentage:")
            print(val)
            print("Difference from actual data:")
            difference = ((m * 4 + b) - val)
            print(difference)
            print("----------------------------------------------")
            print("\n")
            
            if difference >= 0:
                total += difference
            else:
                total -= difference
            i += 1

        print("Average difference:")
        print(total / 30)


        

test = toArray()
testValues = toArray.getTestValues()
trainingValues = toArray.getTrainingValues()
teamNames = toArray.getTeamNames()

toArray.makePrediction()