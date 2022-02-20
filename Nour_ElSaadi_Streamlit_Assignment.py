import streamlit as st
import numpy as np
import pandas as pd
import plotly as plt
import plotly.express as px
import plotly.io as pio
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("milk-production-tonnes-assignment1.csv")

st.image("https://images.unsplash.com/photo-1618338423029-cf13f0cbe809?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=918&q=80")

st.markdown(' # Welcome to the world of Milk!')
st.markdown(' ###### Hello! Welcome to a world built by Nour El Saadi, an MSBA student who recently joined a new venture that revolves around farming. The more she read about milk production, the more her interest in the topic increased. She then thought of creating this Streamlit app as a means to communicate her findings around global milk production!' )
st.markdown(' ### Do you like milk and want to know more about the world of milk?' )

df["Code"].fillna("Continent", inplace = True)
newdf= df
newdf= newdf.loc[newdf['Code'] == 'Continent']
newdf=newdf.drop(['Code'], axis=1)
  
newdfregion= newdf
array = ['Oceania', 'Asia', 'Africa', 'Americas', 'Europe']
newdfregion= newdfregion.loc[newdfregion['Entity'].isin(array)]
figure1 = px.bar(newdfregion, x="Entity", y="Milk Production (Tonnes)", color="Entity",
animation_frame="Year", range_y=[0,400000000], title= 'Production of Milk by region')
#other plot
newdfsum= newdf
newdfsum= newdfsum.groupby('Year').sum('Milk Production (Tonnes)')
newdfyear= pd.DataFrame(newdfsum)
newdfyear= newdfyear.reset_index()
data = [go.Bar(x=newdfyear['Year'], y=newdfyear['Milk Production (Tonnes)'])]
layout=go.Layout(title='Global Milk Production throughout the Years', xaxis=dict(title='Year'), yaxis= dict(title='Milk Production (Tonnes)'))
figure2=go.Figure(data=data, layout=layout)
#other plot
fig=px.choropleth(df,locations="Code", animation_frame="Year", animation_group="Code", color="Milk Production (Tonnes)", color_continuous_scale= px.colors.diverging.BrBG,hover_name= "Entity",  title = "Global Milk Production")

agree = st.radio(
     "",
     ('Yes, I do!', 'No, I\'m not interested...'))

if agree == 'Yes, I do!':
     st.success('Buckle Up! We\'re going on a trip to teach you about Milk Production!')
     st.plotly_chart(figure2, use_container_width=True)
     with st.expander("See explanation"):
         st.write(""" The chart above shows how global milk production has skyrocketed in just about 60 years. """)
     st.markdown(' #### Now, how would you like to learn more about global milk production?' )

     container = st.container()
     all = st.checkbox("Select all")
     if all:
         selected_options = container.multiselect("Select one or more options:",
         ['Region-Based Bar plot', 'World Map'], ['Region-Based Bar plot', 'World Map'])
         st.plotly_chart(figure1, use_container_width=True)
         with st.expander("See explanation"):
             st.write(""" The chart above indicates that in 1961, Europe was the leading region when it came to milk production. The scene quickly changed around the 1990s as the Americas and Asia were catching up on Europe's milk production, only for Asia to become the leading milk producer by 2005. """)
         st.plotly_chart(fig, use_container_width=True)
         with st.expander("See explanation"):
              st.write(""" When clicking on the play button, one notices how milk production drastically increases around the world. Several countries end up joining the so-called milk production competition! In 2018, India is the leading milk producer! """)
         if st.button('Press me'):
             st.success('Congratulations!')
             st.balloons()
            
    
     else:
         selected_options =  container.multiselect("Select one or more options:",['Region-Based Bar plot', 'World Map']) 
         if 'Region-Based Bar plot' in selected_options:
             st.plotly_chart(figure1, use_container_width=True)
             with st.expander("See explanation"):
                 st.write(""" The chart above indicates that in 1961, Europe was the leading region when it came to milk production. The scene quickly changed around the 1990s as the Americas and Asia were catching up on Europe's milk production, only for Asia to become the leading milk producer by 2005. """)
         if 'World Map' in selected_options:
             st.plotly_chart(fig, use_container_width=True)
             with st.expander("See explanation"):
                 st.write(""" When clicking on the play button, one notices how milk production drastically increases around the world. Several countries end up joining the so-called milk production competition! In 2018, India is the leading milk producer! """)
         if 'Region-Based Bar plot' and 'World Map' in selected_options:
             if st.button('Press me!'):
                 st.success('Congratulations!')
                 st.balloons()
     
else:
    st.info('Well...')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
         st.image("https://media1.giphy.com/media/7k2LoEykY5i1hfeWQB/giphy.gif?cid=ecf05e471lldm5o2g2hgr2qoxq0mvynri3jbiwzaxnw17a3i&rid=giphy.gif&ct=g")
    with col3:
        st.write('')

    st.info('We still believe you must at the very least visually see how numbers have been varying in the world of milk production, so there you go:')

    st.plotly_chart(figure2, use_container_width=True)
    st.plotly_chart(figure1, use_container_width=True)
    st.plotly_chart(fig, use_container_width=True)
    if st.button('Press me'):
        st.success('This was not too hard, right? Congratulations on learning about milk production!')
        st.balloons()
    
