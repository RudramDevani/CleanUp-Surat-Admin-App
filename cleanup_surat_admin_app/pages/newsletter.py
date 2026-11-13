import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"].split("/rest/v1")[0].rstrip("/")
    return create_client(url, st.secrets["SUPABASE_KEY"])

sb = init_connection()

tab = 'newsletter'

st.title("Newsletter Inquiry Page", text_alignment="center")
st.text("Here you will get the data of Inquires for newsletters", text_alignment="center")

rows = sb.table(tab).select('*').execute().data
st.dataframe(pd.DataFrame(rows), hide_index=True)

news_info = st.text_input('Enter the "id" here you want to delete the data')

if st.button('Delete The Data'):
    sb.table(tab).delete().eq('id', news_info).execute()
    st.success('Data removed')
