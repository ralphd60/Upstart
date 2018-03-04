import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def upstart_data():
    df = pd.read_csv\
        ('C:\\Users\\ralphd60\\Downloads\\performance.csv',sep=',',parse_dates=True,index_col='Origination Date')
    df_portfolio =  pd.read_csv\
        ('C:\\Users\\ralphd60\\Downloads\\Upstart_Investor_Portfolio_20180303_Desiderio.csv',sep=',',parse_dates=True,index_col='Issue Date')
    # creates a new data frame with just 2 columns
    # this is need as I cant find a way to filter out NaN data in just one column
    data = df[['Loan Grade', 'Loan Size','Charged Off Date']]

    # Then I drop the Nan of Charge Off Date
    # In place by assigning it to itself
    data = data.dropna()
    grade = ['AAA','AA','A','B','C','D','E']

    # Count the number of loans in each grade and the number of discharged loans
    # then the las chart will show the percentage
    # data_port = df_portfolio.groupby('Grade')['Grade'].count() / df_portfolio['Grade'].count() * 100
    # data_all = df.groupby('Loan Grade')['Loan Grade'].count() / df['Loan Grade'].count() * 100
    # data_discharged = data.groupby('Loan Grade')['Loan Grade'].count() / data['Loan Grade'].count() * 100
    # data_combine = round(data.groupby('Loan Grade')['Loan Grade'].count() / df.groupby('Loan Grade')['Loan Grade'].count()  * 100, 2)

    # This calulates by loan size
    data_port = df_portfolio.groupby('Grade')['Investment Amount'].sum() / df_portfolio['Investment Amount'].sum() * 100
    data_all = df.groupby('Loan Grade')['Loan Size'].sum() / df['Loan Size'].sum() * 100
    data_discharged = data.groupby('Loan Grade')['Loan Size'].sum() / data['Loan Size'].sum() * 100
    data_combine = round(data.groupby('Loan Grade')['Loan Size'].sum() / df.groupby('Loan Grade')['Loan Size'].sum()  * 100, 2)


    # I HAVE SET UP THE SUBPLOT GRAPHS 2 DIFFERENT WAYS
    # ONE USING AXES OBJECT, AND ONE JUST USING PLT OBJECT
    # plt.subplot(4, 1, 1)

    # This graph is for total loans Upstart originated
    fig, axes = plt.subplots(nrows=4, ncols=1)
    fig.canvas.set_window_title('Upstart.com')
    data_all = data_all.reindex(index=grade)
    data_all.plot(ax=axes[0],kind='bar', color='green')

    for i in axes[0].patches:
        # get_width pulls left or right; get_y pushes up or down
        axes[0].text(i.get_x() + .09, i.get_height() + .5, \
                str(np.round(i.get_height(),decimals=1)) + '%', fontsize=7, color='black')

    axes[0].set_xticks([])
    axes[0].set_xlabel('')
    # plt.xticks(rotation='horizontal')
    axes[0].grid(axis='y', color='black', linestyle='-', linewidth=.5)
    axes[0].set_ylabel('All(% of)')
    axes[0].set_ylim(0, 50)


    # plt.subplot(4, 1, 2)
    # This graph is for My Portfolio
    data_port = data_port.reindex(index=grade)
    data_port.plot(ax=axes[1],kind='bar', color='yellow')

    # set individual bar labels using above list
    for i in axes[1].patches:
        print(i)
        # get_width pulls left or right; get_height pushes up or down
        axes[1].text(i.get_x() + .09, i.get_height() + .5, \
                str(np.round(i.get_height(),decimals=1)) + '%', fontsize=7, color='black')
    axes[1].set_xticks([])
    axes[1].set_xlabel('')
    # plt.set_xticks(rotation = 'horizontal')
    axes[1].grid(axis='y', color='black', linestyle='-', linewidth=.5)
    axes[1].set_ylabel('Port(% of)')
    axes[1].set_ylim(0, 50)

    # plt.subplot(4, 1, 3)
    # This graph is for ratio of all dischardes broken down by gradd
    data_discharged = data_discharged.reindex(index=grade)
    data_discharged.plot(ax=axes[2], kind='bar', color='red')
    for i in axes[2].patches:
        # get_width pulls left or right; get_height pushes up or down
        axes[2].text(i.get_x() + .09, i.get_height() + .5, \
                     str(np.round(i.get_height(), decimals=1)) + '%', fontsize=7, color='black')
    axes[2].set_xticks([])
    axes[2].set_xlabel('')
    # plt.xticks(rotation='horizontal')
    axes[2].grid(axis='y',color='black', linestyle='-', linewidth=.5)
    axes[2].set_ylabel('Dis(% of)')
    axes[2].set_ylim(0, 50)

    #plt.subplot(4, 1, 4)
    # This graph is for All discharges against all Originations
    data_combine = data_combine.reindex(index=grade)
    data_combine.plot(kind='bar',color='blue')
    for i in axes[3].patches:
        # get_width pulls left or right; get_height pushes up or down
        axes[3].text(i.get_x() + .09, i.get_height() + .5, \
                     str(np.round(i.get_height(), decimals=1)) + '%', fontsize=7, color='black')


    axes[3].grid(axis='y', color='black', linestyle='-', linewidth=.5)
    axes[3].set_ylabel('Dis/All')
    axes[3].set_ylim(0,50)
    plt.xticks(label='Loan Grade', rotation='horizontal')
    plt.suptitle('Micro Loans (Original Amount)',fontsize=16)

    # plt.tight_layout()
    plt.show()


upstart_data()