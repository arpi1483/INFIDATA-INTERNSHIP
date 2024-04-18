import streamlit as st
import datetime

st.header('student registration form')
my_form=st.form(key='form-1')
fname=my_form.text_input('enter the first name:')
lname=my_form.text_input('enter the last name:')
email=my_form.text_input('enter the email:')
mobile=my_form.text_input('enter the mobile no:')
gender=my_form.radio('gender',('male','female'))
age=my_form.slider('Age',1,100)
DOB=my_form.date_input('enter the dob:',min_value=datetime.date(1990,1,1))
address=my_form.text_area('enter the address:')
resume=my_form.file_uploader('upload your resume:')
my_form.form_submit_button('submit')

st.write('first name:',fname)
st.write('last name:',lname)
st.write('email :',email)
st.write('mobile no:',mobile)
st.write('gender is:',gender)
st.write('age is:',age)
st.write('dob is:',DOB)
st.write('address is:',address)