import requests
import json
import urllib2
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from urllib2 import urlopen
from bs4 import BeautifulSoup


response = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0001/")
url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
#test = json.load(response)
#print test
data = response.json()
get = urlopen(url)
json_object = json.load(get)
#int(type(data))


url2 = "http://steamsales.rhekua.com/view.php?steam_type=app&steam_id=238010"
r = requests.get(url2)
data = r.text
soup = BeautifulSoup(data, "html.parser")
#steampage = BeautifulSoup(urllib2.urlopen('https://steamdb.info/app/22380/').read(), "html.parser")
pricehistory = soup.findAll("div", { "class" : "tab_price" })
datahistory = soup.findAll("div", { "class" : "genre_release"})

data = {
    'history' : [],
}
data2 = {
    'history2' : []
}
tempPrice = 0.00
prices = []
lowestPrice = 999999999.99
highestPrice = 0.00
counter = 0
for row in pricehistory:
    cols = pricehistory
    insert = cols[counter].get_text()
    indices = [pos for pos, char in enumerate(insert) if char == '$']
    insert2 = insert[indices[0] + 1: indices[1]]
    insert3 = insert[indices[1] + 1: ]
    insert = insert[indices[1] + 1: ]

    tempPrice = float(insert2)
    tempPrice2 = float(insert)
    prices.append ( tempPrice )
    data['history'].append( insert )
    if tempPrice2 < lowestPrice:
        lowestPrice = tempPrice2
    if tempPrice > highestPrice:
        highestPrice = tempPrice
    counter += 1
    #print tempPrice
    #print tempPrice2
#print data['history'][0]
print "Lowest Price for Deus Ex: Human Revolution: " + str(lowestPrice)
print "Highest Price for Deus Ex: Human Revolution: " + str(highestPrice)
print "Current Price for Deus Ex: Human Revolution: " + str(data['history'][0])
print "Original Price for Deus Ex: Human Revolution: " + str(highestPrice)

for row in datahistory:
    cols = datahistory
    data2['history2'].append( cols[0].get_text() )
print data2['history2'][0].strip()



for Apps in json_object['applist']['apps']['app']:
    if (Apps['appid'] == 292030):
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
        getdlc = requests.get(
            'http://store.steampowered.com/api/appdetails/?appids=%d&cc=us' % Apps['appid'])

        #cookie = {'steamLogin': '76561198307902452%7C%7C2496BAA1FDB8A863861D8A2EF251FAACFBF760E5'}
        #params = {'country': 'US', 'currency': 1, 'appid': Apps['appid'], 'market_hash_name': urllib2.quote(Apps['name'])}
        #gethistory = requests.get('http://steamcommunity.com/market/pricehistory', params=params, cookies = cookie)
        #print(gethistory.text)

        if getprice.status_code == 200:
            rjson = json.loads(getprice.text)
            djson = json.loads(getdev.text)
            pjson = json.loads(getpub.text)
            tjson = json.loads(getdate.text)
            mjson = json.loads(getscore.text)
            gjson = json.loads(getgenre.text)
            #hjson = json.loads(gethistory.text)
            dlcjson = json.loads(getdlc.text)
            # use the appid to fetch the value and convert to decimal
            # appid is numeric, cast to string to lookup the price
            try:
                price = rjson[str(Apps['appid'])]['data']['price_overview']['initial'] * .01
            except:
                price = 0
            try:
                developer = djson[str(Apps['appid'])]['data']['developers'][0]
            except:
                developer = 'N/A'
            try:
                publisher = pjson[str(Apps['appid'])]['data']['publishers'][0]
            except:
                publisher = 'N/A'
            try:
                date = tjson[str(Apps['appid'])]['data']['release_date']['date']
            except:
                date = 'N/A'
            try:
                score = mjson[str(Apps['appid'])]['data']['metacritic']['score']
            except:
                score = 'N/A'
            try:
                genre = gjson[str(Apps['appid'])]['data']['genres'][0]['description']
            except:
                genre = 'N/A'
            #try:
            #    history = hjson[0]
            #except:
            #    history = 'N/A'
            try:
                dlc = dlcjson[str(Apps['appid'])]['data']['dlc']
                #print dlc
            except:
                dlc = 'N/A'

            Apps[Apps['appid']] = {'appID': Apps['appid'],'name': Apps['name'], 'price': price, 'developer': developer, 'publisher': publisher, 'date': date, 'score': score, 'genre': genre}
            print Apps[Apps['appid']]
            Apps[Apps['appid']] = {'dlc': dlc}
            print Apps[Apps['appid']]
            """
            for dlcid in dlc:
                Apps[Apps[dlcid]] = {'appID': dlcid, 'name': Apps['name'], 'price': price,
                                       'developer': developer, 'publisher': publisher, 'date': date, 'score': score,
                                       'genre': genre}
                print Apps[Apps[dlcid]]
            """

for Apps in json_object['applist']['apps']['app']:
    if (Apps['appid'] in dlc):
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

        #cookie = {'steamLogin': '76561198307902452%7C%7C2496BAA1FDB8A863861D8A2EF251FAACFBF760E5'}
        #params = {'country': 'US', 'currency': 1, 'appid': Apps['appid'], 'market_hash_name': urllib2.quote(Apps['name'])}
        #gethistory = requests.get('http://steamcommunity.com/market/pricehistory', params=params, cookies = cookie)
        #print(gethistory.text)

        if getprice.status_code == 200:
            rjson = json.loads(getprice.text)
            djson = json.loads(getdev.text)
            pjson = json.loads(getpub.text)
            tjson = json.loads(getdate.text)
            mjson = json.loads(getscore.text)
            gjson = json.loads(getgenre.text)
            #hjson = json.loads(gethistory.text)
            # use the appid to fetch the value and convert to decimal
            # appid is numeric, cast to string to lookup the price
            try:
                price = rjson[str(Apps['appid'])]['data']['price_overview']['initial'] * .01
            except:
                price = 0
            try:
                developer = djson[str(Apps['appid'])]['data']['developers'][0]
            except:
                developer = 'N/A'
            try:
                publisher = pjson[str(Apps['appid'])]['data']['publishers'][0]
            except:
                publisher = 'N/A'
            try:
                date = tjson[str(Apps['appid'])]['data']['release_date']['date']
            except:
                date = 'N/A'
            try:
                score = mjson[str(Apps['appid'])]['data']['metacritic']['score']
            except:
                score = 'N/A'
            try:
                genre = gjson[str(Apps['appid'])]['data']['genres'][0]['description']
            except:
                genre = 'N/A'
            #try:
            #    history = hjson[0]
            #except:
            #    history = 'N/A'

            Apps[Apps['appid']] = {'appID': Apps['appid'],'name': Apps['name'], 'price': price, 'developer': developer, 'publisher': publisher, 'date': date, 'score': score, 'genre': genre}
            print Apps[Apps['appid']]

print(response.status_code)