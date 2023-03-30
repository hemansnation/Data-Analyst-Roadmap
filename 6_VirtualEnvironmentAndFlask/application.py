from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)  # __main__

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

status = response.status_code

# print(status)

content = response.content

soup = BeautifulSoup(content, 'html.parser')

# print(soup.body)
print(soup.title)
print(soup.title.get_text())


@app.route('/')
def hello():
    return "Hello from index route"

@app.route('/home')
def home():
    return "<h1>Welcome User, this is Home</h1>"


@app.route('/profile')
def profile():
    name = "Himanshu"

    return render_template('index.html', n = name)


if __name__ == '__main__':
    app.run(port=5000)





#      https:   //github.com     /hemansnation
#    scheme      DNS              route
# - file    Domain Name System
# - ftp       IP
# - http
# ipv4, ipv6
# API - Application Programming Interface (code/algorithm)
# localhost - IP - 127.0.0.1:5000/hemansnation