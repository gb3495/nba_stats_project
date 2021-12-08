import mysql.connector
import MySQLdb
from MySQLdb import _mysql
from mysql.connector import connect, errorcode
import json
import requests
import pandas as pd
import urllib
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#   Simple script to pull data from NBA.com

url = 'https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2013-14&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
           "X-Requested-With" : "XMLHttpRequest",
           "Host" : "stats.nba.com",
           "Referer" : "https://www.nba.com/"}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'html.parser')
print(soup)