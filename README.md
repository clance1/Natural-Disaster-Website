# Programming Paradigms Final Project

Final Project for Programming Paradigms CSE 30332

## Group Members

- Aemile Donoghue (adonoghu)
- Carson Lance (clance1)
- Connor Kuse (ckuse1)
- Jamie Zhang (jzhang17)

## General Overview

Our project is a web application which takes data from various sources of natural disasters and occurrences (e.g. Forest Fires, Tornadoes, Meteor Landings, etc.) over the last 20 years.
This data is then used to generate a visual mapping of historical sites of natural importance or correlation with regard to natural disasters. The data will also be used in a DBSCAN clustering algorithm in order to process the dataset for ease of viewing and outlier detection.

## Usage of API

The main file, _natural_disasters_database.py, is a general class file that imports and uses functions specific to other class files. These files are as listed:

 - tornado_db.py
 - meteor_db.py
 - fires_db.py
 - landslide_db.py

As of completion of the first project milestone, this API is able to make queries through the data based on various factors such as state of occurrence, year/month of occurrence,
and type of occurrence. Since returning certain data based on user queries with specified conditions is a large majority of our project, we found it sufficient to merely include these
functions as of this first milestone. However, there are also quality of life functions such as resetting, deleting, and printing as well.

## Running API Tests

*Because our python library relies on the **panda** package, you would need to install panda first before running the test scripts successfully*
> To install panda, you can type in
>       `pip3 install panda`

To test the API and make sure that all functions are working correctly, the test_api.py file can be run. This will run a series of unit tests on the class files which will test all
used functions. Simply type `python3 test_api.py` to use.

## Usage of Server

The file  main.py is our main webserver, this is a CherryPy server that has controllers that utilize all of the APIs discussed above. Each of the APIs have various actions that can be utilized with REST calls. Specifically each of the disasters have GET and POST functionality.

Each of the GET requests for the server are accessed by appending to the main url the respective natural disaster. For example, `http://student04.cse.nd.edu:PORT/fires/state/CA` will return all of the fires stored in the database that have occured in California.

The POST requests require a JSON to be sent to the main URL for each natural disaster. The JSON must have Latitude and Longitude as the first 2 elements of the request due to the indexing of our database. Upon completion the server will return `{'result': 'success'}`

*Our server uses the **Geopy** package for the latitude and longitude, all scripts will fail until installing this package*
> To install geopy, you can type
>       `pip3 install geopy`

## Running Server Tests

To test the server, the file test_ws.py can be run. This will test the GET and POST requests that are server utilizes. Simply type `python3 test_ws.py` to use.

## Usage of Client

The client has its own folder within the main folder in which there are 2 html files and subfolders for styles and scripts. The index.html will display the main part of the program which is the map that shows all of the different disasters. The add.html contains the forms that will be used for the PUT requests to add new disasters to the API.

In order to use the client run the server using the instructions above and then go to [Link](http://student04.cse.nd.edu/clance1/final/client).

The add methods can be submitted with any manner of elements included however the main program utilizes the latitude and longitude as well as the year.

Below is an example of a pin on the map

<img height="360" src="images/maptest.png">

## Running Client Tests

In order to test the client we added disasters for a year that was not included in our original databases using the forms and then used the main page to display all of the disasters for that year.

## Disaster Clustering

In order to further analyze our data we implemented a Density-Based Spatial Clustering of Applications with Noise (DBSCAN) algorithm. The basis of DBSCAN is that it will parse the data and take certain points of density based on a minimum requirement and search for values within a certain distance away from the center cluster. In addition if a cluster is within the specified distance away from another cluster center then will be combined into one cluster. The values that are not within the specified distance become outliers. In the context of our project we are using the clustering data to check if certain places represented by our data are simply freak occurances or if they are consistently being affected by natural disasters. Using this data the user can decide whether or not to live in a certain area.
This clustering utilizes the **sklearn**, **basemap**, and **folium** libaries so in order to run the **learning.py** you first must `pip install` each of these libraries.

<img src="images/fire_cluster.png" width="360"/> <img src="images/tornado_cluster.png" width="360"/> <img src="images/landslide_cluster.png" width="360">


The black dots represent the outliers in the data while the colored clusters represent where a high concentration of certain disasters take place. This knowledge could be used for future machine learning such as a prediction model.