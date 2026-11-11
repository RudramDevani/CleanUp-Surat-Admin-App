import streamlit as st
import pandas as pd
from supabase import create_client, Client

#page Setup

st.set_page_config(page_title='CleanUp Admin')

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url=st.secrets['SUPABASE_URL']
    key=st.secrets['SUPABASE_KEY']
    return create_client(url, key)

sb = init_connection()

# app setup

st.title('CleanUp Surat Admin App', text_alignment='center')
st.text("Welcome to CleanUp Surat's Admin Page, here, this app will help you out in uploading images in your website, getting the data of volunteers, reported spot, item adoption, etc.")
st.warning("use it wisely as the changes here will affect in the website too.")

@st.cache_resource
def Login():
    adm = st.text_input("User Name", placeholder="Enter Here")
    pwd = st.text_input("Password", type='password')
    User = ['CleanUp1407', 'CleanUp@1407']
    if adm in User and pwd in User:
        return 1
    else:
        return 0

LoginVal = Login()

while LoginVal == 1:
    pg = st.navigation([st.Page('pages/volunteer.py', title='Volunteers'), st.Page('pages/orgianzation.py', title='Organization want to join')])
    pg.run