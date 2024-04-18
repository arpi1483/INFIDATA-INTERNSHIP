import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage=0

def set_state(i):
    st.session_state.stage=i

if st.session_state.stage==0:
    st.button('Begin',on_click=set_state,args=[1])

if st.session_state.stage>=1:
    name=st.text_input('Name',on_change=set_state,args=[2])

if st.session_state.stage>=2:
    st.write('hello',name)
    color=st.selectbox('pick a color',
                       [None,'red','orange','blue','green','violet'],
                       on_change=set_state,args=[3]
                       )
    if color is None:
        set_state(2)

if st.session_state.stage>=3:
    st.write(f':{color}[thank you]')
    st.button('start over',on_click=set_state,args=[0])

