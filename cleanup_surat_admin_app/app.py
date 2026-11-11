import streamlit as st

#page Setup

st.set_page_config(page_title='CleanUp Admin')

# app setup

st.title('CleanUp Surat Admin App', text_alignment='center')
st.text("Welcome to CleanUp Surat's Admin Page, here, this app will help you out in uploading images in your website, getting the data of volunteers, reported spot, item adoption, etc.")
st.warning("use it wisely as the changes here will affect in the website too.")
st.divider()
st.text('This is the app page, use slider to access other pages which are as follows:')
st.text('Volunteer: Here you will get data of all volunteers who have filled the form in the website of CleanUp Surat')
st.text('Organisation: Data of Requests of Organizations who want to join the drive')
st.text('Adoption: Here you will be abel to do both: \n    1) Add the Items for Adoption page \n    2)Get data of who are interested in that applied item')
st.text('Reported Spots: Here you will get the details of the spot which are reported and actions are not taken')
st.text('Add Image: Here You will able to add Images to the gallery of Website')
st.text('Contact: Here you will get the data of the one who have contacted us')
st.text('Events: From this we will be able to add the details of upcomming events in our website')
st.text('Newsletters: Here we will able to get who wants the newsletter from us')

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

st.divider()
st.caption('Created For CleanUp Surat')
st.caption('By Rudram Devani')
st.caption('MailID: rudramdevani1@gmail.com')