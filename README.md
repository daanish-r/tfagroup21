# Squirrel Tracker in Central Park

This app is made to keep a track of all the squirrels in Central Park

Link for the app:

Map - https://tools-for-analytics-2019.appspot.com/map

Sightings - https://tools-for-analytics-2019.appspot.com/sightings

Update - https://tools-for-analytics-2019.appspot.com/update


## Contributors details

Name:

Aditya Baser - Columbia University, Master's in Operations Research

Daanish Rode - Columbia University, Master's in Management Sciences

## Prerequisites

This app is constructed by using the following softwares
1) Django 2.2.7
2) Python 3.7
3) sqlite
4) html5
5) bootstrap

## Importing the data

A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 

python manage.py import_squirrel_data /path/to/file.csv

## Exporting the data

A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 

python manage.py export_squirrel_data /path/to/file.csv

