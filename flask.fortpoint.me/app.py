from flask import Flask, Response, request, render_template
from flask import redirect, url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def home_canonical():
    return render_template('home.html', active='home')


@app.route('/home/')
def home():
    return redirect(url_for('home_canonical'))


@app.route('/story/')
def story():
    return render_template('story.html', active='story')


@app.route('/companies/')
def companies():
    return render_template('companies.html', active='companies')


@app.route('/team/')
def team():
    return render_template('team.html', active='team')


if __name__ == '__main__':
    app.run()
