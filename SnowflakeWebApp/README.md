# Python connector for Snowflake

Snowflake "Data Application Builders 
workshop".  


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) 
to install snowflake connector and sqlalchemy.

```bash
> pip install snowflake-connector-python
> pip install snowflake-sqlalchemy
```

## Hosting a website locally with flask

We'll also install the flask package to 
host a website for reasons that may become 
clear later. Anyway, here's how to do that
```python
from flask import Flask

app = Flask("my website")


@app.route("/")
def hello_world():
    return "<p>Here's a paragraph</p><p>Here's another paragraph</p>"


app.run(debug=True)

```
## Connecting this website to Snowflake

Now we want to read information from our Snowflake
account and display it on this website. Simple 
example is below
```python
# read password from command line
print("enter Snowflake password")
password = input()

# snowflake bits
cnx = connector.connect(
    account='ld05233.eu-west-1',
    user='ShaneShort',
    password=password
)
cur = cnx.cursor()
cur.execute("SELECT current_account()")
one_row = cur.fetchone()

```

## interpreting tables in python with pandas

We've created a test table in Snowflake and
will now read this table using python as:

```python
cur = cnx.cursor()
cur.execute("SELECT * FROM COLOURS")
rows = pd.DataFrame(cur.fetchall(), columns=['Colour UID', 'Colour Name'])
print(rows)

# convert rows to html
dfhtml = rows.to_html()
print(dfhtml)
```
To display this on our website we'll create a 
html template.

## HTML templates
Create the ```index.html``` file in the 
```templates``` directory.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Colours</title>
<head>
<h1>Header</h1>
<body>
<h2> Colours, not colors</h2>
{{dfhtml | safe}}
</html>'''
</body>
</html>
```
Now replace the string of ```html``` in our 
```homepage``` function with the
```render_template```function and
add the ```dfhtml``` arg to render the 
table in our website
```python
@app.route("/")
def homepage():
    return render_template('index.html', dfhtml=dfhtml)
```

## Allow user to add to the table via the website

Create another ```html``` template for 
submitting to 

## License
[Snowflake](https://learn.snowflake.com/courses)