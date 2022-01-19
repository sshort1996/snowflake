from flask import Flask, render_template
from snowflake import connector
import pandas as pd

app = Flask("my website")


@app.route("/")
def homepage():
    return render_template('index.html', dfhtml=dfhtml)

@app.route("/submit")
def submitpage():
    return render_template('submit.html')

# read password from command line
print("enter Snowflake password")
password = input()

# snowflake bits
cnx = connector.connect(
    account='ld05233.eu-west-1',
    user='ShaneShort',
    password=password,
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)
cur = cnx.cursor()
cur.execute("SELECT * FROM COLOURS")
rows = pd.DataFrame(cur.fetchall(), columns=['Colour UID', 'Colour Name'])

# convert rows to html
dfhtml = rows.to_html()

app.run()
