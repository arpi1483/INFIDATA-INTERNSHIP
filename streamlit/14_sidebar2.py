import streamlit as st

st.title('Arithmetic operation')
st.markdown('please give the input')

st.sidebar.title('select the operation')
st.sidebar.markdown('select the option accordingly:')

choice=st.sidebar.selectbox('select',('ADD','MUL'))
selected_status=st.sidebar.selectbox('select number',options=['2n','3n'])

if choice=='ADD':
    if selected_status=='2n':
        n1=st.number_input('enter the n1:')
        n2= st.number_input('enter the n2:')
        sum=n1+n2
        st.success(sum)
    elif selected_status=='3n':
        n1 = st.number_input('enter the n1:')
        n2 = st.number_input('enter the n2:')
        n3=st.number_input('enter the n3:')
        sum = n1 + n2+n3
        st.success(sum)

elif choice=='MUL':
    if selected_status=='2n':
        n1=st.number_input('enter the n1:')
        n2= st.number_input('enter the n2:')
        product=n1*n2
        st.success(product)
    elif selected_status=='3n':
        n1 = st.number_input('enter the n1:')
        n2 = st.number_input('enter the n2:')
        n3=st.number_input('enter the n3:')
        product = n1*n2*n3
        st.success(product)



