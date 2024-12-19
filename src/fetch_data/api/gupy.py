import json

from fetch_data.api.fetch import fetchdata

import pandas as pd
import requests


def fetchdata(label: str) -> dict:
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

    r = requests.get(url)
    response = r.json()
   
    return response

labels = ['dados', 'UX/UI', 'administração', 'rh', 'frontend']

all_jobs = []
for l in labels:
    fetch_data = fetchdata(l)
    df_jobs_data = pd.DataFrame((fetch_data)['data'])
    all_jobs.append(df_jobs_data)

df_jobs = pd.concat(all_jobs, ignore_index=True)
df_jobs = df_jobs.replace(r'^\s*$', 'Dado Não Disponível', regex=True)

# Creating job_type column
a_dados = ['dados']
a_uxui = ['uxui', 'ux ui', 'ux/ui']
a_adm = ['adm', 'administração', 'administracao']
a_rh = ['rh', 'recursos humanos']
a_frtend = ['frontend']

def check_category(x):
    if any(keyword  in x.lower() for keyword in a_dados):
        return 'DADOS'
    elif any(keyword  in x.lower() for keyword in a_uxui):
        return 'UX/UI'
    elif any(keyword  in x.lower() for keyword in a_adm):
        return 'ADM'
    elif any(keyword  in x.lower() for keyword in a_rh):
        return 'RH'
    elif any(keyword  in x.lower() for keyword in a_frtend):
        return 'FRTEND'
    else:
        return 'DADO NÃO IDENTIFICADO'

df_jobs['job_type'] = df_jobs['name'].apply(check_category)

# Creating exprience column
a_intern = ['estagiário', 'estágio', 'estagio', 'estagiario']
a_junior = ['junior', 'jr', 'júnior']
a_basic = ['pleno', 'pl']
a_senior = ['senior', 'sr', 'sênior']

def check_experience(x):
    if any(keyword in x.lower() for keyword in a_intern):
        return 'ESTAGIO'
    elif any(keyword in x.lower() for keyword in a_junior):
        return 'JUNIOR'
    elif any(keyword in x.lower() for keyword in a_basic):
        return 'PLENO'
    elif any(keyword in x.lower() for keyword in a_senior):
        return 'SENIOR'
    else:
        return 'DADO NÃO IDENTIFICADO'
    
df_jobs['experience'] = df_jobs['name'].apply(check_experience)
    
df_jobs