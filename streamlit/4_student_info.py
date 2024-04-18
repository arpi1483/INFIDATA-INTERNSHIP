import streamlit as st
name=st.text_input('enter the name:')
branch=st.text_input('enter the branch:')
id=st.number_input('enter the stud id:')
t1=st.number_input('enter the t1 marks:')
t2=st.number_input('enter the t2 marks:')
t3=st.number_input('enter the t3 marks:')
average=(t1+t2+t3)/3
st.write('the name is:',name)
st.write('the branch is:',branch)
st.write('the id is:',id)
st.write('the t1 marks is:',t1)
st.write('the t2 marks is:',t2)
st.write('the t3 marks is:',t3)
st.write('the average marks is:',average)

