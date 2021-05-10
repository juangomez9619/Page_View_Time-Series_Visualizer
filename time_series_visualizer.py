#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df[
    (df.value <= df.value.quantile(0.975)) &
    (df.value >= df.value.quantile(0.025))
]
#%%

def draw_line_plot():
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = (9,4)
    plt.plot(df.index,df.value, color='red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(by=[df.index.year, df.index.month]).agg({'value':'mean'})
    df_bar.index.set_names(["Years", "Months"], inplace=True)
    df_bar.reset_index(inplace=True)


        
    df_bar['Months']= df_bar.apply(
    lambda row: number_to_name(row['Months']),
    axis=1)
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 9))
    sns.barplot(
        data = df_bar,
        x = 'Years',
        y = 'value',
        hue = 'Months',
        hue_order=['January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'],
        palette="tab10"
    )
    plt.legend(loc='upper left')
    plt.ylabel('Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename(columns={'value':'Page Views'}, inplace=True)
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(18,9))

    sns.boxplot(
    x='Year',
    y='Page Views',
    data = df_box,
    ax = ax[0]  
    )

    ax[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(
    x='Month',
    y='Page Views',
    data = df_box,
    ax = ax[1],
    order=['Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec']
    )
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
#%%
def number_to_name(month):
    number_name = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
    }
    return number_name[month]

# %%
