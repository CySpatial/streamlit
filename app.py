import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

markdown = """
Bu uygulama Mustafa Ceyhan tarafından
hazırlanmıştır.
"""

st.sidebar.title("Hakkında")
st.sidebar.info(markdown)
logo = "https://1.bp.blogspot.com/-Ac-V6NYW4ZY/VAmyeqmPBAI/AAAAAAAAUkQ/lQnH9gGLml0/s1600/dunya_uzerinde_turkiye.jpg"
st.sidebar.image(logo)


st.write("GERCEK ZAMANLI AMENAJMAN PLAN UYGULAMASI")

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

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, layers_control=True,minimap_control=True)
    m.add_basemap(basemap)
    m.set_center(35.888432,39.654455)
    m.add_shp(bascatak,"bascatak_plan_siniri",style=style_b,info_mode=False)
    m.add_shp(culhali,"culhali_plan_siniri",style=style_c,info_mode=False)
  
    

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
    