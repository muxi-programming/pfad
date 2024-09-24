#-*- coding: utf-8 -*-


import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie ,Bar,Timeline


df = pd.read_csv('weather.csv', encoding='gb18030')
print(df['日期'])


df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))
print(df['日期'])


df['month'] = df['日期'].dt.month

print(df['month'])



df_agg = df.groupby(['month','天气']).size().reset_index()
print(df_agg)


df_agg.columns = ['month','tianqi','count']
print(df_agg)


print(df_agg[df_agg['month']==1][['tianqi','count']]\
    .sort_values(by='count',ascending=False).values.tolist())



timeline = Timeline()

timeline.add_schema(play_interval=1000)


for month in df_agg['month'].unique():
    data = (

        df_agg[df_agg['month']==month][['tianqi','count']]
        .sort_values(by='count',ascending=True)
        .values.tolist()
    )

    bar = Bar()

    bar.add_xaxis([x[0] for x in data])

    bar.add_yaxis('',[x[1] for x in data])


    bar.reversal_axis()

    bar.set_series_opts(label_opts=opts.LabelOpts(position='right'))

    bar.set_global_opts(title_opts=opts.TitleOpts(title='2023 hongkong weather'))

    timeline.add(bar, f'{month}月')


print("开始生成 HTML 文件")
timeline.render(r'C:\Users\沐汐\Desktop\hk_weathers.html')
print("HTML 文件生成完毕")




