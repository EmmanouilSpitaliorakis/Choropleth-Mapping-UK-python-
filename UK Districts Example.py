import json
import pandas as pd
import plotly.express as px
from urllib.request import urlopen

with urlopen('https://opendata.arcgis.com/datasets/3b374840ce1b4160b85b8146b610cd0c_0.geojson') as response:
    uk_districts = json.load(response)
    
pop_data=pd.read_csv("ons2data.csv")

#Have a look at the data and the GeoJSON file to find a mapping identifier you can use

pop_data.head()
uk_districts['features'][0]['properties']

#Here we can use the column "name" in the population data and 
#"LAD20NM" in the feature properties

fig = px.choropleth_mapbox(pop_data, locations="name", featureidkey="properties.LAD20NM", geojson=uk_districts, color="Median Age", hover_name="name", mapbox_style="carto-positron", zoom=4, center = {"lat": 55, "lon": 0})
fig.show()
