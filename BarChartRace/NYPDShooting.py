import pandas as pd 
import bar_chart_race as bcr

#bcr.__version__

#Importing Data
df = pd.read_csv('Data/NYPD_Shooting_Incident_Data__Historic_.csv')
df = df[['OCCUR_DATE','BORO']]
#print(df)
#print(df.info())

#Formatting the dataset 
df['OCCUR_DATE'] = pd.to_datetime(df['OCCUR_DATE'])
data = df.groupby('OCCUR_DATE')['BORO'].value_counts().unstack().fillna(0)
data=data.astype(int)
data=data.cumsum()

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    print(data)


#Bar Chart Race
bcr.bar_chart_race(
    df=data,
    filename='NYPD_Shooting_Incident.mp4',
    orientation='h',
    sort='desc',
    steps_per_period=50,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %-d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total shootings: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    period_length=50,
    figsize=(5, 3),
    dpi=144,
    cmap='accent',
    title='NYPD Shooting Incidents by Borough',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'Tahoma', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)