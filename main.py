from utils.dataframe import df_jobs

import pandas as pd
import streamlit as st
import plotly.express as px

df_jobs_per_state = (df_jobs.groupby(['state', 'job_type'])
                     .agg(
                         job_quantity = ('job_type', 'count')
                         )
                         .reset_index()
)


fig = px.bar(df_jobs_per_state,
       x = 'state',
       y = 'job_quantity',
       color = 'job_type',
       labels = {
        'state': 'Estados', 
        'job_quantity': ' ', 
        'job_type': 'Tipo de Vaga',
         },
         barmode= 'group',
         title= 'Relação de Quantidade de Vagas por Estado'
       )

fig = fig.update_traces(textfont_size=6, textangle=90, cliponaxis=False)

df_jobs_workplace_type_count = (df_jobs.groupby(['state', 'job_type'])
                .agg(
                    workplace_type_count = ('workplaceType', 'value_counts')
                ).reset_index()
    )

fig2 = px.bar(
    df_jobs_workplace_type_count,
    x= 'workplaceType',
    y = 'workplace_type_count',
    color= 'job_type',
    labels = {
        'workplaceType': 'Tipo de Vaga',
        'workplace_type_count': 'Valores',
    },
    barmode='group',
    title= 'Relação Entre Quantidade e Forma de Trabalho'
)

st.plotly_chart(fig)
st.write('Vemos grande concentração de vagas de emprego em São Paulo e também\
          em locais onde os dados não foram encontrados')
st.divider()

col1, col2 = st.columns(2)

col1.plotly_chart(fig2)