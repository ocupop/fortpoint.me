from flask import Flask, Response, request, render_template
from flask import redirect, url_for, request
from subprocess import Popen
from os.path import abspath, dirname, join
import json
import settings
import re

HERE = dirname(abspath(__file__))

app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route('/')
def home_canonical():
    return render_template('home.html', active='home')

@app.route('/home/')
def home():
    return redirect(url_for('home_canonical'))


@app.route('/clients/')
def clients():
    return render_template('clients.html', active='clients')

@app.route('/companies/')
def companies():
    return redirect(url_for('clients'))


@app.route('/story/')
def story():
    return render_template('story.html', active='story')


@app.route('/team/')
def team():
    return render_template('team.html', active='team')


@app.route('/connect/')
def connect():
    return render_template('connect.html', active='connect')


@app.route('/github-webhook', methods=['POST'])
def pull_latest():

    # Ignore requests that don't specify the expected GitHub secret (preventing
    # unauthorized triggering of site updates)
    if request.args['secret'] != settings.github_secret:
        return ''

    payload = json.loads(request.form['payload'])

    # Only consider the "master" branch and branches that are prefixed with
    # "preview-"
    match = re.search('^refs/heads/(preview-[a-zA-Z0-9_/-]+|master)$',
        payload['ref'])

    if not match:
        return ''

    # Check out the changed branch. If it's been deleted, then revert to the
    # master branch
    branchname = match.group(1)
    if payload['deleted'] and payload['forced']:
        branchname = 'master'

    script = join(HERE, '..', 'pull-and-restart.sh')

    # Fork a new process to update the site so that this request can be
    # correctly terminated
    try:
        Popen([script, branchname])
    except:
        pass

    return ''

if __name__ == '__main__':
    app.run()
