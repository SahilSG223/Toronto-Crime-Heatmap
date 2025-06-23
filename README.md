**Toronto Crime Heat-Map
**

Visualise 2024 assault + robbery rates for every Toronto neighbourhood on an interactive, zoomable web map built with pandas · GeoPandas · Folium.

This repo turns two open datasets—Toronto neighbourhood polygons and crime counts—into a heat-map HTML file you can open in any browser or embed in a web page. The workflow:

Read & clean the CSV (assault + robbery, 2024).

Merge with the GeoJSON neighbourhood boundaries.

Normalise rates ⟶ 0‒1 weights.

Render a Folium/Leaflet map with a semi-transparent heat-layer.

Toronto Open Data portal → Neighbourhood_Crime_Rates.csv

Wide format (one column per crime+year)

Neighbourhood Boundaries

Toronto Open Data portal → Neighbourhoods.geojson

Already in WGS-84 (EPSG: 4326)

Data © City of Toronto. Used under Toronto Open Data Licence.
