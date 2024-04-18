import streamlit as st
percentage=st.number_input('enter the percentage:')

if(percentage>90):
    st.success('grade A')

elif(percentage>80 and percentage<=90):
    st.success('grade B')

elif(percentage>=60 and percentage<=80):
   st.success('grade C')

elif(percentage<=60):
   st.success('grede D')


