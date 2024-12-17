from utils.dataframe import df_jobs

import pandas as pd
import streamlit as st

list_of_data = df_jobs['job_type'].unique()

select_vagas = st.sidebar.pills('Filtro de Áreas', 
            options=list_of_data,
            selection_mode='multi',
        )
vagas_selector = df_jobs[df_jobs['job_type'].isin(select_vagas)]

if vagas_selector.empty:
    st.warning('Selecione ao menos uma área')
else:
    for _,row in vagas_selector.iterrows():
        st.subheader(row['name'])
        col1, col2, col3 = st.columns(3)

        col1.metric('Modelo de Trabalho', row['workplaceType'])
        col2.metric('Estado', row['state'])
        col3.metric('Experiência', row['experience'])
        
        message = st.chat_message('🏢')
        message.write(f'**{row["careerPageName"]}**')
        st.write(row['description'])

        st.divider()
