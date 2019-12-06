from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
#$ pip install Flask-OAuth
import urllib3
import requests
from urllib.parse import urlparse

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = "488806718921-5vhe1f86a1qr84u4ir7v0fod7lq5m317.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "OmaRoGfY1fPb0KOX6-TNNWqr"
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console

SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

google = oauth.remote_app('google',
base_url='https://www.google.com/accounts/',
authorize_url='https://accounts.google.com/o/oauth2/auth',
request_token_url=None,
request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
'response_type': 'code'},
access_token_url='https://accounts.google.com/o/oauth2/token',
access_token_method='POST',
access_token_params={'grant_type': 'authorization_code'},
consumer_key=GOOGLE_CLIENT_ID,
consumer_secret=GOOGLE_CLIENT_SECRET)

@app.route('/')
def index():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

access_token = access_token[0]


headers = {'Authorization': 'OAuth '+access_token}
http = urllib3.PoolManager()
req = http.request('GET','https://www.googleapis.com/oauth2/v1/userinfo')


@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)

@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))

@google.tokengetter
def get_access_token():
    return session.get('access_token')

def main():
    app.run()

if __name__ == '__main__':
    main()