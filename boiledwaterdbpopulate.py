#Author: Joshua Pineda
#Date: 11/26/2017
#Version 1.0
#A script that inserts Steam app information into the boiledwaterdb on PostgreSQL. If you want to use another database, some modifications are needed
import requests
import json
import urllib2
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from urllib2 import urlopen
from bs4 import BeautifulSoup
import psycopg2
#All necessary packages must be installed before running this script. This script was developed on Python 2.7. Code may need changes for a Python 3 interpreter

#Note, this requires an internet connection and PostgreSQL to use
response = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0001/")#Requests to get the data from the API query
url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
#Creates a json object from data pulled from the API
data = response.json()#Gets JSON formatted data from response
get = urlopen(url)#Gets data from URL
json_object = json.load(get)#Loads the JSON object
con = psycopg2.connect(database='boiledwaterdb', user='root', host='localhost', password='root')#Attempt to connect to the PostgreSQL database, you must use these specific settings for your database. Make sure to create the tables beforehand.
con.autocommit = True #Automatically commits the insertion of each row in the database
cur = con.cursor() #Cursor position

#Initializes developer table
developerID = {}
developerID.update({"N/A": 0})
devCount = 0
cur.execute("INSERT into developer(d_id, d_name) VALUES (%s, %s)", (0, "N/A"))
#Initializes publisher table
publisherID = {}
publisherID.update({"N/A": 0})
pubCount = 0
cur.execute("INSERT into publisher(publisher_id, publisher_name)" + "VALUES (%s, %s)", (0, "N/A"))

#Insert data for Apps with AppIDs under 100 and inserts them into games table
for Apps in json_object['applist']['apps']['app']:
    if (Apps['appid'] < 500): #Makes requests to pull data for all apps with ID < 500
        getprice = requests.get('http://store.steampowered.com/api/appdetails/?appids=%d&filters=price_overview&cc=us' % Apps['appid'])
        getdev = requests.get(
            'http://store.steampowered.com/api/appdetails/?appids=%d&filters=developers&cc=us' % Apps['appid'])
        getpub = requests.get(
            'http://store.steampowered.com/api/appdetails/?appids=%d&filters=publishers&cc=us' % Apps['appid'])
        getdate = requests.get(
            'http://store.steampowered.com/api/appdetails/?appids=%d&filters=release_date&cc=us' % Apps['appid'])
        getscore = requests.get(
            'http://store.steampowered.com/api/appdetails/?appids=%d&filters=metacritic&cc=us' % Apps['appid'])
        getgenre = requests.get(
            'http://store.steampowered.com/api/appdetails/?appids=%d&filters=genres&cc=us' % Apps['appid'])
        getsales = requests.get("https://steamspy.com/api.php?request=appdetails&appid=%d" % Apps['appid'])

        #If request query is successful, convert json files into text and store them into lists. Displays all data, and inserts them into games table
        if getprice.status_code == 200:
            rjson = json.loads(getprice.text)
            djson = json.loads(getdev.text)
            pjson = json.loads(getpub.text)
            tjson = json.loads(getdate.text)
            mjson = json.loads(getscore.text)
            gjson = json.loads(getgenre.text)
            sjson = json.loads(getsales.text)
            # use the appid to fetch the value and convert to decimal
            # appid is numeric, cast to string to lookup the price
            # Use try and except statements when extracting the data for each attribute
            try:
                price = rjson[str(Apps['appid'])]['data']['price_overview']['initial'] * .01
                price = float(price)
            except:
                price = 0.00
            try:
                developer = djson[str(Apps['appid'])]['data']['developers'][0]
                developer = str(developer)
            except:
                developer = 'N/A'
            try:
                publisher = pjson[str(Apps['appid'])]['data']['publishers'][0]
                publisher = str(publisher)
            except:
                publisher = 'N/A'
            try:
                date = tjson[str(Apps['appid'])]['data']['release_date']['date']
                date = str(date)
            except:
                date = 'N/A'
            try:
                score = mjson[str(Apps['appid'])]['data']['metacritic']['score']
                score = float(score)
            except:
                score = 0.00
            try:
                genre = gjson[str(Apps['appid'])]['data']['genres'][0]['description']
                genre = str(genre)
            except:
                genre = 'N/A'
            try:
                sales = sjson['players_forever']
            except:
                sales = 0

            #Creates a new entry in Developers table if current developer doesn't exist
            if developer not in developerID:
                devCount += 1
                developerID[developer] = devCount
                #Assign an ID to developer
                cur.execute("INSERT into developer(d_id, d_name)" + "VALUES (%s, %s)", (developerID[developer],
                            developer))
            #Creates a new entry in the Publishers table if current publisher doesn't exist
            if publisher not in publisherID:
                pubCount += 1
                publisherID[publisher] = pubCount
                #Assign an ID to publisher
                cur.execute("INSERT into publisher(publisher_id, publisher_name)" + "VALUES (%s, %s)", (publisherID[publisher],
                            publisher))
            games = [int(Apps['appid']), str(Apps['name']), date, genre, developerID[developer], publisherID[publisher], sales, price, score]
            print games
            #Insert data into games table
            cur.execute("INSERT into games(app_id, app_name, released, genre, developer, publisher, sales, price, score)" +  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", games)
            print "Data inserted."

#Handles the DLC fetching and inserting for the database
for Apps in json_object['applist']['apps']['app']:
    if (Apps['appid'] < 500):#Gets the DLCs connected to all Apps with AppID < 500
        getdlc = requests.get('http://store.steampowered.com/api/appdetails/?appids=%d&cc=us' % Apps['appid'])
        AppID = Apps['appid']
        if (getdlc.status_code == 200):
            dlcjson = json.loads(getdlc.text)
            try:
                dlc = dlcjson[str(Apps['appid'])]['data']['dlc']
                print str(Apps['name'])
                # print dlc
            except:
                dlc = []
            print dlc

            # Insert data for DLC connected to Apps with AppIDs under 100 and inserts them into DLC table
            for Apps in json_object['applist']['apps']['app']:
                tempID = int(Apps['appid'])
                if (tempID in dlc):#Check if an AppID corresponds to a DLC ID
                    getprice = requests.get(
                        'http://store.steampowered.com/api/appdetails/?appids=%d&filters=price_overview&cc=us' % Apps[
                            'appid'])
                    getdate = requests.get(
                        'http://store.steampowered.com/api/appdetails/?appids=%d&filters=release_date&cc=us' % Apps[
                            'appid'])
                    getsales = requests.get("https://steamspy.com/api.php?request=appdetails&appid=%d" % Apps['appid'])

                    # If request query is successful, convert json files into text and store them into lists. Displays all data, and inserts them into DLC table
                    if getprice.status_code == 200:
                        rjson = json.loads(getprice.text)
                        tjson = json.loads(getdate.text)
                        sjson = json.loads(getsales.text)
                        # use the appid to fetch the value and convert to decimal
                        # appid is numeric, cast to string to lookup the price
                        try:
                            price = rjson[str(Apps['appid'])]['data']['price_overview']['initial'] * .01
                            price = float(price)
                        except:
                            price = 0.00
                        try:
                            date = tjson[str(Apps['appid'])]['data']['release_date']['date']
                            date = str(date)
                        except:
                            date = 'N/A'
                        try:
                            sales = sjson['players_forever']
                        except:
                            sales = 0

                        DLC = [int(Apps['appid']), int(AppID), str(Apps['name']), price, date, sales]
                        print DLC
                        # Insert data into dlc table
                        cur.execute(
                            "INSERT into dlc(dlc_id, app_id, dlc_name, price, release_date, sales)" + "VALUES (%s, %s, %s, %s, %s, %s)", DLC)
                        print "Data inserted."


#Inserts pricing history data for Apps with AppIDs under 100 and inserts them into History table
for Apps in json_object['applist']['apps']['app']:
    if (Apps['appid'] < 500):

        url2 = "http://steamsales.rhekua.com/view.php?steam_type=app&steam_id=%d"
        r = requests.get(url2 % Apps['appid'])#Gets history data from the query
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        # steampage = BeautifulSoup(urllib2.urlopen('https://steamdb.info/app/22380/').read(), "html.parser")
        pricehistory = soup.findAll("div", {"class": "tab_price"})#Scrapes price data from HTML
        datahistory = soup.findAll("div", {"class": "genre_release"})#Scrapes timestamp data from HTML

        data = {
            'history': [], #Used to hold prices at a timestamp
        }
        data2 = {
            'history2': [] #Used to hold timestamp data
        }
        tempPrice = 0.00
        prices = []
        lowestPrice = 999999999.99
        highestPrice = 0.00
        counter = 0
        for row in pricehistory:
            cols = pricehistory
            insert = cols[counter].get_text() #Extracts the data from the HTML
            indices = [pos for pos, char in enumerate(insert) if char == '$'] #Look for prices, strings start with $
            insert2 = insert[indices[0] + 1: indices[1]] #Used for lowest/reduced prices
            insert3 = insert[indices[1] + 1:]
            insert = insert[indices[1] + 1:] #Used for highest/non-discounted prices

            tempPrice = float(insert2)
            tempPrice2 = float(insert)
            prices.append(tempPrice)
            data['history'].append(insert)
            #Optional code: Used to find the highest and lowest prices of all time for an item
            if tempPrice2 < lowestPrice:
                lowestPrice = tempPrice2
            if tempPrice > highestPrice:
                highestPrice = tempPrice
            counter += 1

        #Formats the date information
        for row in datahistory:
            cols = datahistory
            timestamp = row.get_text()
            timestamp = timestamp.split(" ", 1)
            formattedDate = timestamp[0]
            data2['history2'].append(formattedDate)

        dates = []

        #Removes spacing from date strings
        for index in data2['history2']:
            index = index.strip()
            dates.append(index)
            #print index

        counter = 0
        #Inserts all history data for an app into the database
        while (counter < data['history'].__len__()):
            history = [int(Apps['appid']), data['history'][counter], dates[counter]]
            #print sales
            print history
            #Insert data into history table
            cur.execute("INSERT into history(app_id, price, yearmonth)" +  "VALUES (%s, %s, %s)", history)
            print "Data inserted."
            counter += 1
