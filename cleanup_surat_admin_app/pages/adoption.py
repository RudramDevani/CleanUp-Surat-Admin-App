import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"].split("/rest/v1")[0].rstrip("/")
    return create_client(url, st.secrets["SUPABASE_KEY"])

sb = init_connection()

tab1 = "items"
tab2 = "item_adoptions"

# page setup

st.title("Adopt-an-Item Page", text_alignment="center")
st.text("Here you will able to know about the adoption items inquiries the people want to adopt, also you will able to add items for adoption", text_alignment="center")

st.subheader("Inquires for Adoption0")

rows = sb.table(tab2).select('*').execute().data
st.dataframe(pd.DataFrame(rows), hide_index=True)

inq_id = st.text_input('Enter the "id" here you want to delete the data')

if st.button('Delete The Data'):
    sb.table(tab2).delete().eq('id', inq_id).execute()
