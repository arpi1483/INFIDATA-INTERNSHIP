import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Stroke prediction dashboard')
st.markdown('Th dashboard will help a research to get to know\ more about the given datsets and its output')

st.sidebar.title('Select visual charts')
st.sidebar.markdown('Select the charts/plots accordingly')

data=pd.read_csv('demo_data_set.csv')

chart_visual=st.sidebar.selectbox('select charts/plot type',
                                  ('line chart','bar chart','bubble chart'))

st.sidebar.checkbox('show analysis by smocking status',True,key=1)
selected_status=st.sidebar.selectbox('select smocking status',
                                     options=['Formerly_smocked','Smokes','Never_Smoked','Unknown'])

fig=go.Figure()
if chart_visual=='line chart':
    if selected_status=='Formerly_smocked':
        fig.add_trace(go.Scatter(x=data.Country ,y=data.formerly_smoked,mode='lines',name='Formerly_Smocked'))
    elif selected_status=='Smokes':
        fig.add_trace(go.Scatter(x=data.Country ,y=data.Smokes,mode='lines',name='Smokes'))
    elif selected_status=='Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country ,y=data.Never_Smoked,mode='lines',name='Never_Smoked'))
    elif selected_status=='Unknown':
        fig.add_trace(go.Scatter(x=data.Country ,y=data.Unknown,mode='lines',name='Unknown'))



elif chart_visual=='bar chart':
    if selected_status=='Formerly_smocked':
        fig.add_trace(go.Bar(x=data.Country, y=data.formerly_smoked, name='Formerly_Smocked'))
    if selected_status=='Smokes':
        fig.add_trace(go.Bar(x=data.Country, y=data.Smokes, name='Smokes'))
    if selected_status=='Never_Smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.Never_Smoked, name='Never_Smoked'))
    if selected_status=='Unknown':
        fig.add_trace(go.Bar(x=data.Country , y=data.Unknown,name='Unknown'))


if chart_visual=="bubble chart":
    if selected_status=='Formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,
                                 mode="markers",
                                 marker_size=[40,60,80,60,40,50],
                                 name='Formerly_smoked'))
    elif selected_status=='Smokes':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Smokes,
                                 mode="markers",
                                 marker_size=[40,60, 80, 60, 40, 50],
                                 name='Smokes'))

    elif selected_status=='Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Never_Smoked,
                                 mode="markers",
                                 marker_size=[40,60, 80, 60, 40, 50],
                                 name='Never_Smoked'))

    elif selected_status=='Unknown':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Unknown,
                                 mode="markers",
                                 marker_size=[40,60, 80, 60, 40, 50],
                                 name='Unknown'))
st.plotly_chart(fig,use_container_width=True)
