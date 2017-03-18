#The solution is based on the Haversine formula

import math


def calculateDistance(city1_lat, city1_lon, city2_lat, city2_lon):
	R = 6371; #metres
	latDiff = math.radians(city2_lat - city1_lat)
	lonDiff = math.radians(city2_lon - city1_lon)
	a = math.sin(latDiff/2)**2 + math.cos(math.radians(city1_lat))*math.cos(math.radians(city2_lat))*(math.sin(lonDiff/2)**2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
	d = R*c
	print(str(d)) 

if __name__ == "__main__":
	city1 = input('Enter lat,lon of city 1 : ')
	city1_lat, city1_lon = city1.split(",")
	city2 = input('Enter lat,lon of city 2 : ');
	city2_lat, city2_lon = city2.split(",")
	calculateDistance(float(city1_lat), float(city1_lon), float(city2_lat), float(city2_lon))

