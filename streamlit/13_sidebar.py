import streamlit as st

add_selectbox=st.sidebar.selectbox('How would u like to be contacted',
                                   ('Email','home phone','mobile')
                                   )

with st.sidebar:
    add_radio=st.radio(
        'choose a shipping method',
        ('standard(5-15days)','expess(2-5days)')
    )
    name=st.text_input('enter the customer name:')