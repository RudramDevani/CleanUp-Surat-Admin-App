import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url=st.secrets['SUPABASE_URL']
    key=st.secrets['SUPABASE_KEY']
    return create_client(url, key)

sb = init_connection()

st.title('Volunteers Page Management', text_alignment='center')
st.text('Here you will get he data of Volunteers who want to join', text_alignment='center')

rows = sb.table('volunteers').select('*').execute().data
st.dataframe(pd.DataFrame(rows))
