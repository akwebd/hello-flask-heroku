from flask import Flask
import notify
app = Flask(__name__)



@app.route('/')
def mail():
    notify
    return 'sent'


if __name__ == '__main__':
    app.run()
