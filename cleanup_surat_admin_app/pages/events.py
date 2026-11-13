import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"].split("/rest/v1")[0].rstrip("/")
    return create_client(url, st.secrets["SUPABASE_KEY"])

sb = init_connection()

tab = 'events'

# page setup

st.title("Upcomming Event Page", text_alignment="center")

st.title("Contact Info Page", text_alignment="center")
st.text('Here you will get the data of the people tried to contact', text_alignment='center')

rows = sb.table(tab).select('*').execute().data
st.dataframe(pd.DataFrame(rows), hide_index=True)

evnt_id = st.text_input('Enter the "id" here you want to delete the data')

if st.button('Delete The Data'):
    sb.table(tab).delete().eq('id', evnt_id).execute()
    st.success("Data removed")

# add events

st.subheader('Add Upcomming Events')

uet = st.text_input('Title')
ued = st.text_area('Description')
uedt = st.datetime_input('Date and Time of Event')
uel = st.text_input('Location')

if st.button('Add Upcomming Event'):
    sb.table(tab).insert({'title': uet, 'descripton': ued, 'date': uedt, 'location': uel}).execute()
    st.success("Data Added")
