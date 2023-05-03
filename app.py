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

style_b = {
    "stroke": True,
    "color": "red",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "red",
    "fillOpacity": 0,
}

style_c = {
    "stroke": True,
    "color": "yellow",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "red",
    "fillOpacity": 0,
}


with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, toolbar_control=True,minimap_control=True)
    m.add_basemap(basemap)
    m.set_center(35.888432,39.654455)
    m.add_shp(bascatak,style=style_b)
    m.add_shp(culhali,style=style_c)
    

    m.add_labels(
        bascatak,
        "SEFLIK_ADI",
        font_size="8pt",
        font_color="red",
        font_family="arial",
        font_weight="bold",
    )

    m.add_labels(
    culhali,
    "SEFLIK_ADI",
    font_size="8pt",
    font_color="yellow",
    font_family="arial",
    font_weight="bold",
)
    m.to_streamlit(height=700)
    