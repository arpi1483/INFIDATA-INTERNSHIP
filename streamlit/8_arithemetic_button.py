import streamlit as st

if 'clicked1' not in st.session_state:
    st.session_state.clicked1=False

if 'clicked2' not in st.session_state:
    st.session_state.clicked2=False

def click_button1():
    st.session_state.clicked1=True
    st.write('Add Button Clicked')

def click_button2():
    st.session_state.clicked2=True
    st.write('Add Button Clicked')

st.button('ADD',on_click=click_button1)
st.button('SUB',on_click=click_button2)

if(st.session_state.clicked1):
    st.title('ADDITION OF TWO NUMBERS')
    n1=st.number_input('enter the n1:')
    n2=st.number_input('enter the n2:')
    sum=n1+n2
    st.info('Addition of 2 number is:')
    st.success(sum)

if(st.session_state.clicked2):
    st.title('SUBSTRACTION OF TWO NUMBERS')
    n1 = st.number_input('enter the n1 :')
    n2 = st.number_input('enter the n2 :')
    sub = n1-n2
    st.info('substraction of 2 number is:')
    st.success(sub)


