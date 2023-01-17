import folium
import fiona
from shapely.geometry import shape

# Create a map object
m = folium.Map(location=[19.416334085596525, -99.07473572701159], zoom_start=16, no_zoom = True)

# open the shapefile
with fiona.open("metro_shp\STC_Metro_estaciones_utm14n.shp") as src:
    # extract the coordinates of the stations
    for feature in src:
        geom = feature['geometry']
        coordinates = geom['coordinates'][:2]
        print(coordinates)
        name = feature['properties']['NOMBRE']
        # Add a marker for the station
        folium.Marker(coordinates, tooltip=name).add_to(m)

# Show the map
m.save("mapa_metro.html")