import pandas as pd 
import bar_chart_race as bcr

#Importing Data
df = pd.read_csv('Data/urban_pop.csv')

#Convert year to datetime and set it as index
df['year']=pd.to_datetime(df.year, format='%Y')
df=df.set_index("year")
#print(df)

#Visualize
bcr.bar_chart_race(
    df=df,
    filename='UrbanPopulation.mp4',
    orientation='h',
    sort='desc',
    steps_per_period=20,
    interpolate_period=False,
    label_bars=True,
    n_bars=8,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total Population: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    period_length=50,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='Urban Population by Country',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'Tahoma', 'color' : '.1'},
    scale='linear',
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)