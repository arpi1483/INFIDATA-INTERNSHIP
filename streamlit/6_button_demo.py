import streamlit as st

animal_shelter=['cat','dog','rabbit','tiger']

animal=st.text_input('type the animal name:')

if st.button('check avilability'):
    have_it=animal.lower() in animal_shelter
    if(have_it):
        st.info('we have the animal')
    else:
        st.info('we dont have the animal')