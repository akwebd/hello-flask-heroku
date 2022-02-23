from flask import Flask
import notify
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/mail')
def mail():
    return notify


if __name__ == '__main__':
    app.run()
