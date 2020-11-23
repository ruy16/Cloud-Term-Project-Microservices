import argparse
import collections
import csv
import json
import glob
import math
from math import radians, cos, sin, asin, sqrt
import os
import pandas
import re
import requests
import string
import sys
import time
import xml

class Bike():
    def __init__(self, baseURL, station_info, station_status):
        # initialize the instance
        self.baseURL = baseURL
        self.station_info = baseURL + station_info
        self.station_status = baseURL + station_status
        #save the json datas
        self.station_info_data = json.loads(requests.get(self.station_info,verify=False).content)
        self.station_status_data = json.loads(requests.get(self.station_status,verify=False).content)

    def total_bikes(self):
        # return the total number of bikes available
        result = 0
        for data in self.station_status_data['data']['stations']:
            result += data['num_bikes_available']
        return result

    def total_docks(self):
        # return the total number of docks available
        result = 0
        for data in self.station_status_data['data']['stations']:
            result += data['num_docks_available']
        return result

    def percent_avail(self, station_id):
        # return the percentage of available docks
        try:
            for data in self.station_status_data['data']['stations']:
                if  int(data['station_id']) == station_id:
                    avi_docks = data['num_docks_available']
                    avi_bikes = data['num_bikes_available']
                    print((avi_docks/(avi_bikes+avi_docks)))
                    return "{}%".format(math.floor((avi_docks/(avi_bikes+avi_docks))*100))
            return ''
        except: # Not found or invalid
            return ""

    def closest_stations(self, latitude, longitude):
        # return the stations closest to the given coordinates
        distances = []
        #top_three = [[0.0,None,None],[0.0,None,None],[0.0,None,None]]
        dist_mapp = dict()
        result = dict()
        for data in self.station_info_data['data']['stations']:
            dist = self.distance(latitude,longitude,data['lat'],data['lon'])
            distances.append(dist)
            dist_mapp[dist] = [data['station_id'],data['name']]

        for i in range(3):
            id = dist_mapp[sorted(distances)[i]][0]
            name = dist_mapp[sorted(distances)[i]][1]
            result[id] = name

        return result


    def closest_bike(self, latitude, longitude):
        # return the station with available bikes closest to the given coordinates
        min_dist = [0,None,None]
        result = dict()
        # Filter the stations with avaliable bikes > 0
        avaliable_bikes = dict()
        for data in self.station_status_data['data']['stations']:
            aval = data['num_bikes_available']
            if int(aval) != 0:
                avaliable_bikes[data['station_id']] = 1
        for item in self.station_info_data['data']['stations']:
            if item['station_id'] in avaliable_bikes:
                d = self.distance(latitude,longitude,item['lat'],item['lon'])
                if min_dist[0] == 0:
                    min_dist[0] = d
                elif d < min_dist[0]:
                    min_dist[0] = d
                    min_dist[1] = item['station_id']
                    min_dist[2] = item['name']

        result[min_dist[1]] = min_dist[2]
        return result
        
    def station_bike_avail(self, latitude, longitude):
        # return the station id and available bikes that correspond to the station with the given coordinates
        station_id = 0
        for data in self.station_info_data['data']['stations']:
            if float(data['lon']) == longitude and float(data['lat']) == latitude:
                station_id = data['station_id']
                break
        for data in self.station_status_data['data']['stations']:
            if data['station_id'] == station_id:
                return {(data['station_id']):int(data['num_bikes_available'])}
        return {}
        

    def distance(self, lat1, lon1, lat2, lon2):
        p = 0.017453292519943295
        a = 0.5 - math.cos((lat2-lat1)*p)/2 + math.cos(lat1*p)*math.cos(lat2*p) * (1-math.cos((lon2-lon1)*p)) / 2
        return 12742 * math.asin(math.sqrt(a))


# testing and debugging the Bike class

if __name__ == '__main__':
    instance = Bike('https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en', '/station_information.json', '/station_status.json')
    print('------------------total_bikes()-------------------')
    t_bikes = instance.total_bikes()
    print(type(t_bikes))
    print(t_bikes)
    print()

    print('------------------total_docks()-------------------')
    t_docks = instance.total_docks()
    print(type(t_docks))
    print(t_docks)
    print()

    print('-----------------percent_avail()------------------')
    p_avail = instance.percent_avail(000) # replace with station ID
    print(type(p_avail))
    print(p_avail)
    print()

    print('----------------closest_stations()----------------')
    c_stations = instance.closest_stations(40.444618, -79.954707) # replace with latitude and longitude
    print(type(c_stations))
    print(c_stations)
    print()

    print('-----------------closest_bike()-------------------')
    c_bike = instance.closest_bike(40.444618, -79.954707) # replace with latitude and longitude
    print(type(c_bike))
    print(c_bike)
    print()

    print('---------------station_bike_avail()---------------')
    s_bike_avail = instance.station_bike_avail(40.445834, -79.954707) # replace with exact latitude and longitude of station
    print(type(s_bike_avail))
    print(s_bike_avail)
