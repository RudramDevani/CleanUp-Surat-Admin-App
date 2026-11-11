import streamlit as st

#page Setup

st.set_page_config(page_title='CleanUp Admin')

# app setup

st.title('CleanUp Surat Admin App', text_alignment='center')
st.text("Welcome to CleanUp Surat's Admin Page, here, this app will help you out in uploading images in your website, getting the data of volunteers, reported spot, item adoption, etc.")
st.warning("use it wisely as the changes here will affect in the website too.")
st.divider()

pg = st.navigation([
    st.Page('pages/volunteer.py', title="Volunteers Management"),
    st.Page('pages/organization.py', title="Organization Management"),
    st.Page('pages/adoption.py', title="Adopt-an-Item"),
    st.Page('pages/reported_spot.py', title="Spots Reported"),
    st.Page('pages/image_add.py', title="Add Images"),
    st.Page('pages/contact_info.py', title="Contacts"),
    st.Page('pages/events.py', title="Upcomming Events"),
    st.Page('pages/newsletter.py', title="Newsletters Inquiry")
])
pg.run()
st.divider()
st.caption('Created For CleanUp Surat')
st.caption('By Rudram Devani')
st.caption('MailID: rudramdevani1@gmail.com')
