import csv
import urllib2
import json
import sys

f = open('androidpackagenames.csv')
fp = open('googleplayscraperoutput.csv', 'wb')
reader = csv.reader(f)
writer = csv.writer(fp, delimiter=',')

accesstoken = raw_input("Please enter your 42matters access_token: ")
print "You entered the access token: ", accesstoken

writer.writerows([['Android Package Name', 'Publisher Name', 'App Name', 'Primary Category', 'Store URL']])




for row in reader:

        try:
                response = urllib2.urlopen('https://data.42matters.com/api/v2.0/android/apps/lookup.json?p=' + ', '.join(map(str, row)) + '&access_token=' + accesstoken)
                appjson = response.read()
                appdata = json.loads(appjson)

                if (appdata.get('app_availability') != 0) :
                        aid = row[0]
                        #print android package name
                        pubname = (appdata['developer'])
                        #print pubname
                        appname = (appdata['title'])
                        #print appname
                        pgenre = (appdata['category'])
                        #print pgenre
                        murl = (appdata['market_url'])
                        separator = '&referrer'
                        cleanmurl = murl.split(separator, 1)[0]
                else:
                        aid = row[0]
                        pubname = 'NULL'
                        appname = 'NULL'
                        pgenre = 'NULL'
                        cleanmurl = 'NULL'

        except urllib2.HTTPError as e:
                aid = row[0]
                pubname = 'NULL'
                appname = 'NULL'
                pgenre = 'NULL'
                cleanmurl = 'NULL'

        writer.writerows([[aid, pubname.encode('utf-8'), appname.encode('utf-8'), pgenre, cleanmurl]])

print "Script run complete. Please check the output googleplayscraperoutput.csv"
