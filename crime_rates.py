import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap
from branca.colormap import linear

data = pd.read_csv('Neighbourhood_Crime_Rates.csv')
data.columns = data.columns.str.strip().str.upper() # Remove spaces, and set columns to all capital letters

keep_cols = ["HOOD_158", "ASSAULT_RATE_2024", "ROBBERY_RATE_2024"]

crime = data.loc[:, ["HOOD_158", "ASSAULT_RATE_2024", "ROBBERY_RATE_2024"]].copy()

crime["CRIME_RATE"] = crime["ASSAULT_RATE_2024"] + crime["ROBBERY_RATE_2024"] # Using rates rather than count

crime = crime[["HOOD_158", "CRIME_RATE"]]

neighbourhoods = gpd.read_file('Neighbourhoods.geojson').to_crs(4326) # Reading geojson file

neighbourhoods["AREA_SHORT_CODE"] = neighbourhoods["AREA_SHORT_CODE"].astype(str)
crime["HOOD_158"] = crime["HOOD_158"].astype(str)

merged = neighbourhoods.merge(crime, left_on="AREA_SHORT_CODE",
                              right_on="HOOD_158",
                              how="left")
merged["CRIME_RATE"].fillna(0, inplace=True) # If neighbourhood is missing
#inplace modifies object called upon rather than returning a new one

# Anchor point for every neighbourhood, so folium HeatMap can plot a dot
merged["lon"] = merged.geometry.centroid.x
merged["lat"] = merged.geometry.centroid.y

minimum_val = merged["CRIME_RATE"].min()
maximum_val = merged["CRIME_RATE"].max()

merged['weight'] = (merged["CRIME_RATE"] - minimum_val) / (maximum_val - minimum_val)


toronto = [43.70, -79.40]
mapObj = folium.Map(location=toronto, tiles='cartodbpositron', zoom_start=10)

heat_data = merged[['lat', 'lon', 'weight']].values.tolist()
HeatMap(heat_data, radius=22, blur=15, max_zoom=12).add_to(mapObj)

mapObj.save("toronto_crime.html")
