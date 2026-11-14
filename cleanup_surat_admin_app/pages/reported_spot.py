import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"].split("/rest/v1")[0].rstrip("/")
    return create_client(url, st.secrets["SUPABASE_KEY"])

sb = init_connection()

tab = "reports"

# page setup

st.title("Spot Reported Page", text_alignment="center")
st.text("Here You will get the data of all the reported spots where waste management is yet to done", text_alignment="center")

rows = sb.table(tab).select('*').execute().data
st.dataframe(pd.DataFrame(rows), hide_index=True)

spt_id = st.text_input('Enter the "id" here you want to delete the data')

if st.button('Delete The Data'):

    delurl_list = sb.table(tab).select('image_url').eq('id', spt_id).execute().data
    if delurl_list[0]['image_url'] != None:
        delurl = delurl_list[0]['image_url']
        pathlist = delurl.split(',')
        path = []
        for i in pathlist:
            templist = i.split('/')
            temppath = templist[-1]
            path.append(temppath)

        sb.table(tab).delete().eq('id', spt_id).execute()
        sb.storage.from_('reports').remove(path)
        st.success("Data removed")
    else:
        sb.table(tab).delete().eq('id', spt_id).execute()
        st.success("Data removed")

# image getting

url_row = sb.table(tab).select("id", "image_url").execute().data

st.subheader("Get Images for Spot")
img_id = st.text_input("Enter the id for images for that spot")

for i in url_row:
    if i['id'] == img_id:
        img_url = i['image_url']
        if img_url != None:
            st.link_button(label="Click for Image", url=img_url)
        else:
            st.text("No Image attached!")
