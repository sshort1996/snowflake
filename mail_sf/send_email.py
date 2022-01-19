import win32com.client
import pandas as pd
from snowflake import connector
import csv
import os


def main():

    # read SnowFlake login from command line
    print("enter Snowflake password")
    password = input()

    # set up python connector
    cnx = connector.connect(
        account='ld05233.eu-west-1',
        user='ShaneShort',
        password=password,
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC'
    )
    cur = cnx.cursor()
    cur.execute("SELECT * FROM COLOURS")  # read all entries from table of dummy data
    rows = pd.DataFrame(cur.fetchall(), columns=['Colour UID', 'Colour Name'])

    # convert rows to csv
    df_csv = rows.to_csv()

    # save csv to disk temporarily
    with open('df_csv.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(df_csv)

    # initiate Outlook app
    outlook = win32com.client.Dispatch('outlook.application')
    # create mail object
    mail = outlook.CreateItem(0)
    print("created mail object")
    # set mail attributes
    mail.To = 'shane.short@clearstrategy.ie'
    mail.Subject = 'Test Email'
    mail.Body = "This is the normal body"
    mail.Attachments.Add(os.getcwd() + '/df_csv.csv')

    # send mail
    mail.Send()
    print("sent mail")

    # delete temp file
    os.remove('df_csv.csv')


if __name__ == '__main__':
    main()
