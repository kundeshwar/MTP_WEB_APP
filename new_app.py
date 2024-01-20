#-------------------------------------------------------import your labrary here 
import streamlit as st
#from deta import Deta
import pandas as pd 
#import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu



st.set_page_config(page_title="Air Pollution Source Inventory", page_icon="", initial_sidebar_state="expanded")

st.sidebar.title(f"Welcome To")
with st.sidebar:
            option = "KP MTP"
            st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)
            st.markdown("------------------")
            option_m_1 = option_menu("SELECT MODE", options=["View Data", "Add Data"], default_index=1)
            st.markdown("------------------")
            option_m = option_menu("SELECT SOURCE", options=["AREA SOURCE", "LINE SOURCE", "POINT SOURCE"], default_index=1)
            st.markdown("------------------")
            choice = st.selectbox('Select the Year?', ('2009','2015','2020','2022', "2024"))
        #--------------------------------had 
        # --- HIDE STREAMLIT STYLE ---
hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)
            
        #---------------------------------------------headline for app
option = "Air Pollution Source Inventory"
st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)
if option_m_1 == "Add Data" and option_m == "LINE SOURCE":
        st.markdown("------------------")
        option = "Line Source"
        st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)
        choice = st.selectbox(

        'Select the Category of Vehicle?',

        ('2 wheelers','3 Wheelers','Car diesel','Car Petrol','HDDV', "Taxies", "others"))
        with st.form("entry_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with st.expander("ID"):
                    link_1_h = st.text_area("write here 🔽", placeholder="Source ID up to 12 characters ...")
                with st.expander("Desc"):
                    link_2_h = st.text_area("write here 🔽", placeholder="Optional description ...")
                with st.expander("SourceID_Prefix"):
                    link_3_h = st.text_area("write here 🔽", placeholder="Text prefix up to 4 characters long for generated LINE_VOLUME and LINE_AREA sources ...")
                with st.expander("Base_Elev"):
                    link_4_h = st.text_area("write here 🔽", placeholder="Source base elevation above mean sea level ...")
                with st.expander("Height"):
                    link_5_h = st.text_area("write here 🔽", placeholder="Release height above ground ...")
                with st.expander("Diam"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Inner stack diameter (POINT) or circular area radius (AREA_CIRC) ...")
                with st.expander("Exit_Vel"):
                    link_7_h = st.text_area("write here 🔽", placeholder="Exit velocity (POINT only)...")
                with st.expander("Exit Temp"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Exit temperature (POINT only) ...")
                with st.expander("Release Type"):
                    link_6_h = st.text_area("write here 🔽", placeholder="VERTICAL, HORIZONTAL, CAPPED (POINT only) - HORIZONTAL and CAPPED are non-default beta options ...")
                with st.expander("SigmaY"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Initial sigma Y (VOLUME only)   ...")
                with st.expander("SigmaZ"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Initial sigma Z (AREA, AREA_CIRC, AREA_POLY, VOLUME, LINE, and LINE_AREA only; optional for AREA, AREA_CIRC, AREA_POLY, and LINE)   ...")
                with st.expander("Rotation_Angle"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Clockwise rotation from North of Y side (AREA and OPEN PIT only)...")
                with st.expander("Length_X"):
                    link_6_h = st.text_area("write here 🔽", placeholder="X side length (AREA, VOLUME, OPEN PIT, and LINE_AREA only; optional for VOLUME, will be used to calculate SigmaY) ...")
                with st.expander("Length_Y"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Y side length (AREA and OPEN PIT only); width for LINE sources ...")
                submitted = st.form_submit_button("Save Data")
                
        



