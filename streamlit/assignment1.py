import streamlit as st
import datetime

st.header('student registration form')
my_form=st.form(key='form-1')
fname=my_form.text_input('enter the first name:')
lname=my_form.text_input('enter the last name:')
email=my_form.text_input('enter the email:')
mobile=my_form.text_input('enter the mobile no:')
gender=my_form.radio('gender',('male','female'))
DOB=my_form.date_input('enter the dob:',min_value=datetime.date(1990,1,1))
address=my_form.text_area('enter the address:')
city=my_form.text_input('enter the city name:')
areaPIN=my_form.text_input('enter the pin:')
state=my_form.text_input('enter the state:')
qualification=my_form.selectbox('select qualification',['MCA','BCA','BTech','BSC'])
specialization1=my_form.checkbox('Java')
specialization2=my_form.checkbox('Web')
password=my_form.text_input('enter your password:')
my_form.form_submit_button('Registratered')
