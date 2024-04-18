import streamlit as st
cname=st.text_input('enter the cname:')
cid=st.text_input('enter the cid:')
unit=st.number_input('enter the units:')

if(unit<=100):
    price=unit*0
    st.write('electricity charges is:',price)

elif(unit>=100 and unit<=200):
    price=(unit-100)*5
    st.write('electricity charges is:', price)

elif(unit>=200):
    price=(unit-100)*10
    st.write('electricity charges is:', price)
