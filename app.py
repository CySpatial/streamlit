import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://www.turkeyholidaydiary.com/wp-content/uploads/2013/12/turkey-tourist-map-1.jpg"
st.sidebar.image(logo)


st.write("AMENAJMAN PLAN UYGULAMASI")

col1, col2 = st.columns([5, 1])
options = list(leafmap.basemaps.keys())
index = options.index("SATELLITE")

bascatak="./shapeFile/bascatak4326.shp"
culhali="./shapeFile/culhali4326.shp"

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    m.add_basemap(basemap)
    m.set_center(35.888432,39.654455)
    m.add_shp(bascatak)
    m.add_shp(culhali)
    m.to_streamlit(height=700)
    