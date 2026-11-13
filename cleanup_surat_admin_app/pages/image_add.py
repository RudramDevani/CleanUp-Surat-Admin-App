import streamlit as st
import pandas as pd 
from supabase import create_client, Client

# Supabase Setup

@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"].split("/rest/v1")[0].rstrip("/")
    return create_client(url, st.secrets["SUPABASE_KEY"])

sb = init_connection()

st.title("Add Image Page", text_alignment="center")
st.text("Here you will be able to manage the gallery by uploading the photos of drive", text_alignment='center')

fldr = st.selectbox("Select the Folder", ['after','before','events','volunteers'])

imglist  = sb.storage.from_('gallery').list(fldr)
datatab = []
for i in imglist:
    rowdict = {}
    rowdict['name']=i['name']
    rowdict['id']=i['id']
    datatab.append(rowdict)
st.dataframe(pd.DataFrame(datatab), hide_index=True)

try:
    imag = st.file_uploader("Upload Photo")
    iname = imag.name.replace(' ','_')
    if imag and st.button("Upload Image"):
        sb.storage.from_('gallery').upload(
            path=f'{fldr}/{iname}',
            file=imag.getvalue(),
            file_options={'content-type': imag.type, "upsert": 'true'}
        )
        st.success('Image Uploaded')
except Exception:
    st.error('Upload Image')
