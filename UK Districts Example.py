import json
import pandas as pd
import plotly.express as px
from urllib.request import urlopen

link_to_map = 'https://opendata.arcgis.com/datasets/3b374840ce1b4160b85b8146b610cd0c_0.geojson'

with urlopen(link_to_map) as response:
    uk_districts = json.load(response)
    
pop_data=pd.read_csv("ons2data.csv")

#Printing the dataframe and the the GeoJson to find relationships.
print(pop_data.head())
print(uk_districts['features'][0]['properties'])

#After checking the data we found a relationship for the City names, 
#the dataframe column name for the cities is: "City"
#and for the GeoJson it is: "LAD20NM"


#Creating the map figure
fig = px.choropleth_mapbox(pop_data, locations="name", featureidkey="properties.LAD20NM",
                           geojson=uk_districts, color="Median Age", hover_name="name", mapbox_style="carto-positron",
                           zoom=4, center = {"lat": 55, "lon": 0})
fig.show()
