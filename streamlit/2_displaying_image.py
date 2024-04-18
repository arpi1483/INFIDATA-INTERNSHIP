import streamlit as st
from PIL import Image
img=Image.open('images.jpg')
img2=Image.open('IMG20230619232659.jpg')
st.title('Displaying IMAGE')
st.image(img,width=750)
st.title('Displaying KALLU IMAGE')
st.image(img2,width=850)