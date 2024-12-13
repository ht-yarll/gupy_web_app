from fetch import fetchdata

import pandas as pd


labels = ['dados', 'UX/UI', 'administração', 'rh', 'frontend']

all_jobs = []
for l in labels:
    fetch = fetchdata(l)
    df_jobs_data = pd.DataFrame((fetch)['data'])
    all_jobs.append(df_jobs_data)

df_jobs = pd.concat(all_jobs, ignore_index=True)