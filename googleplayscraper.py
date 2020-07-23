import csv
import urllib2
import json
import sys
import time

f = open('androidpackagenames.csv')
fp = open('googleplayscraperoutput.csv', 'wb')
reader = csv.reader(f)
writer = csv.writer(fp, delimiter=',')

accesstoken = raw_input("Please enter your 42matters access_token: ")
print "You entered the access token: ", accesstoken

writer.writerows([['Android Package Name', 'Publisher Name', 'Website', 'App Name', 'Primary Category', 'Store URL']])




for row in reader:

        try:
                response = urllib2.urlopen('https://data.42matters.com/api/v2.0/android/apps/lookup.json?p=' + ', '.join(map(str, row)) + '&access_token=' + accesstoken)
                appjson = response.read()
                appdata = json.loads(appjson)

                if (appdata.get('app_availability') != 0) :
                        aid = row[0]
                        #print android package name
                        pubname = appdata.get('developer')
                        if pubname is None:
                                pubname = "NA"
                        #print pubname
                        website = appdata.get('website')
                        if website is None:
                                website = "NA"
                        #print website
                        appname = appdata.get('title')
                        if appname is None:
                                appname = "NA"
                        #print appname
                        pgenre = appdata.get('category')
                        if pgenre is None:
                                pgenre = "NA"
                        #print pgenre
                        murl = appdata.get('market_url')
                        if murl is not None:
                                separator = '&referrer'
                                cleanmurl = murl.split(separator, 1)[0]
                        else:
                                cleanmurl = "NA"
                else:
                        aid = row[0]
                        pubname = 'NULL'
                        website = 'NULL'
                        appname = 'NULL'
                        pgenre = 'NULL'
                        cleanmurl = 'NULL'

        except urllib2.HTTPError as e:
                aid = row[0]
                pubname = 'NULL'
                website = 'NULL'
                appname = 'NULL'
                pgenre = 'NULL'
                cleanmurl = 'NULL'

        writer.writerows([[aid, pubname.encode('utf-8'), website.encode('utf-8'), appname.encode('utf-8'), pgenre, cleanmurl]])
        time.sleep(0.05)
        #to rate limit for 42matters 50 QPS limit

print "Script run complete. Please check the output googleplayscraperoutput.csv"
