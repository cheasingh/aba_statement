import pandas as pd
from datetime import datetime
from pathlib import Path


def convert_to_hbank_format(path_to_xlsx, save_path):
    '''
    this function is designed to convert ABA statement xlsx 
    to HomeBank app csv import format.
    '''

    df = pd.read_excel(path_to_xlsx)
    # format data
    df.columns = df.iloc[1]
    df = df.drop([0, 1])
    df = df.drop(columns=['Ccy', 'Balance'])

    # clean data
    # remove , from thousand number
    df['Money In'] = df['Money In'].str.replace(',', '')
    df['Money Out'] = df['Money Out'].str.replace(',', '')

    # change column object type to float for negative calculation
    df[['Money Out', 'Money In']] = df[['Money Out', 'Money In']].astype(float)

    # format date
    df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')
    df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')

    # fix nan value to 0
    df = df.fillna(0)

    # convert to negative number
    df['Money Out'] *= -1

    # sum for amount column
    df['amount'] = df['Money In'] + df['Money Out']
    new_name = {
        'Date': 'date',
        'Transaction Details': 'info',
    }

    df.rename(columns=new_name, inplace=True)
    df.drop(columns=['Money Out', 'Money In'], inplace=True)

    # add empty columns to match with homebank requirement
    df['category'] = ''
    df['tags'] = ''
    df['payee'] = ''
    df['memo'] = ''
    df['payment mode'] = 4

    # re-arrange the columns
    cols = ['date', 'payment mode', 'info', 'payee',
            'memo', 'amount', 'category', 'tags']
    df = df[cols]

    # export the file
    now = datetime.now()

    file_name = f"homebank_{now.strftime('%d%m%Y')}"

    df.to_csv(f'{save_path}\{file_name}.csv', index=False)

    print(f'file save to: {save_path}\{file_name}.csv')
