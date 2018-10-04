import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
#print(data)
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev): #el is integer
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",
                                     fill_color=color_producer(el), fill=True, color="grey",
                                     fill_opacity=0.7
                                     ))


map.add_child(fg)
map.save("map6.html")