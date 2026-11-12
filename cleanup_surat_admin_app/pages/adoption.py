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

# items putting for adoption

st.subheader("Give for Adoption")

itemrows = sb.table(tab1).select('*').execute().data
st.dataframe(pd.DataFrame(itemrows), hide_index=True)

name = st.text_input("Name of Item")
Des = st.text_area("Description")
cat = st.text_input("Category")
cond = st.text_input("Condition")
fnd_at = st.text_input("Found at")
photo = st.file_uploader('Upload Image of item')
if photo and st.button('Upload Image'):
    sb.storage.from_('items').upload(
        path=photo.name,
        file=photo.getvalue(),
        file_options={'content-type': photo.type, 'upsert': 'true'}
    )
    st.success("Photo uploaded successfully")
photourl = sb.storage.from_('items').get_public_url(photo.name)
stat = st.text_input("Status")

if st.button("Insert the data"):
    sb.table(tab1).insert({'name': name, 'description': Des, 'category': cat, 'condition': cond, 'found_at': fnd_at, 'image_url': photourl, 'status': stat})

item_id = st.text_input('Enter the "id" here you want to delete the data')

if st.button('Delete The Data'):
    sb.table(tab1).delete().eq('id', item_id).execute()
