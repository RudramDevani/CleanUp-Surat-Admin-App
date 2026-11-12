import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"].split("/rest/v1")[0].rstrip("/")
    return create_client(url, st.secrets["SUPABASE_KEY"])

sb = init_connection()

tab = 'volunteers'

st.title('Volunteers Page Management', text_alignment='center')
st.text('Here you will get the data of Volunteers who want to join', text_alignment='center')

rows = sb.table(tab).select('*').execute().data
st.dataframe(pd.DataFrame(rows), hide_index=True)

vol_id = st.text_input('Enter the "id" here you want to delete the data')

if st.button('Delete The Data'):
    sb.table(tab).delete().eq('id', vol_id).execute()
