import streamlit as st

st.sidebar.title('Reg Form')
with st.form(key='Form1'):
    with st.sidebar:
        user_word=st.text_input('enter the keyword:')
        select_language=st.radio('Tweet language',('All','English','hindi'))
        include_retweets=st.checkbox('include retweet in data')
        num_of_tweets=st.number_input('minimum number of tweets',100)
        submitted1=st.form_submit_button(label='search Twitter')

st.write('keyword is:',user_word)
st.write('Language is:',select_language)