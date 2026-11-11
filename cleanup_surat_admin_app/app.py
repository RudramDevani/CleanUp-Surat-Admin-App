import streamlit as st
import pandas as pd
from supabase import create_client, Client

#page Setup

st.set_page_config(page_title='CleanUp Admin')

# app setup

st.title('CleanUp Surat Admin App', text_alignment='center')
st.text("Welcome to CleanUp Surat's Admin Page, here, this app will help you out in uploading images in your website, getting the data of volunteers, reported spot, item adoption, etc.")
st.warning("use it wisely as the changes here will affect in the website too.")

def Login():
    if "AdmDet" not in st.session_state:
        st.session_state.AdmDet = []
    adm = st.text_input("User Name", placeholder="Enter Here")
    pwd = st.text_input("Password", type='password')
    st.session_state.AdmDet.append(adm)
    st.session_state.AdmDet.append(pwd)
    User = ['CleanUp1407', 'CleanUp@1407']
    if st.session_state.AdmDet == User:
        return 1
    else:
        return 0

LoginVal = Login()

if LoginVal == 1:
    pg = st.navigation([st.Page('pages/volunteer.py', title='Volunteers'), st.Page('pages/orgianzation.py', title='Organization want to join')])
    pg.run
else:
    st.text('Wrong User Details')
