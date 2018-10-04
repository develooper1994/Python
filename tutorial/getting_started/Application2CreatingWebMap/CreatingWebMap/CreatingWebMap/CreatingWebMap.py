import folium
import pandas

#print(dir(folium))

#map = folium.Map(location=[80,-100] )
#map.save("Map1.html")

#map = folium.Map(location=[38.58, -99.09] )
#map.save("Map2.html")

#map = folium.Map(location=[38.58, -99.09],zoom_start=6 )
#map.save("Map3.html")

#----------------

#map = folium.Map(location=[38.58, -99.09],zoom_start=6 ,tiles="Mapbox Bright")
#fg=folium.FeatureGroup(name="My Map")

#for coordinates in [[38.2,-99.01],[39.5,-99.5]]:
#    fg.add_child(folium.Marker(location=coordinates, popup="Hi. I am marker",icon=folium.Icon(color="green")) )

#map.add_child(fg)
#map.save("Map4.html")

#----------------
print("-"*50)

data=pandas.read_csv("Volcanoes_USA.txt")
#print(data)
lon = list(data["LON"])
lat = list(data["LAT"])

map = folium.Map(location=[38.58, -99.09],zoom_start=6 ,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi. I am marker",icon=folium.Icon(color="green")) )

map.add_child(fg)
map.save("map5.html")



