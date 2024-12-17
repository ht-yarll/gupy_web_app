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

fig2 = px.histogram(
    df_jobs_workplace_type_count,
    x= 'workplaceType',
    y = 'workplace_type_count',
    color= 'job_type',
    labels = {
        'workplaceType': 'Tipo de Vaga',
        'workplace_type_count': 'Valores',
        'job_type': 'área'
    },
    barmode='group',
    text_auto=True,
    title= 'Relação Entre Quantidade e Forma de Trabalho'
)

fig3 = px.pie(
        df_jobs_workplace_type_count,
        names='workplaceType', 
        values='workplace_type_count',
        facet_col='job_type',
        facet_col_wrap=2,
        facet_col_spacing=0.01,            
        facet_row_spacing=0.2,
        labels={
            'job_type': 'Área',            
            },
        title= 'Modo de Trabalho e Área de Trabalho'
        )


#Building Web App
st.plotly_chart(fig)
st.write('Vemos grande concentração de vagas de emprego em São Paulo e também\
          em locais onde os dados não foram encontrados')
st.divider()

col1, col2 = st.columns(2)

col1.plotly_chart(fig2)
col2.plotly_chart(fig3)
st.write('Fica nítido com a análise dos dados que as áreas de tecnologia\
         vem liderando nos modos de trabalho **remoto** e **híbrido**')