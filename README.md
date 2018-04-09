# Google Play Store Package Name Script
Google Play Store Package Name Script

The purpose of this script is to read a csv of Android package names and output a csv with the parameters

Requirements: python 2.7

Android Package Name
Publisher Name
App Name
Primary Category
Store URL 

This script uses 42 matter's lookup API here: 
https://42matters.com/docs/app-market-data/android/apps/lookup

Steps to execute script:

1. Download the zip file from https://github.com/edwardho/googleplaystoredata

2. Unzip the file and move the folder to your /Desktop directory
 
3. Navigate to Desktop/googleplaystoredata/ and edit the file androidpackagenames.csv and include all the package names you want to look up

    Make sure to only include package names, one per row

    Save the file

4. Open terminal/cmd and enter the command:

    cd Desktop/googleplaystoredata/

5. Enter the command below to run the script on your csv input file:

    python googleplayscraper.py

6. Within the same folder, you should see an output file called "googleplayscraperoutput.csv" which includes the data per package name
