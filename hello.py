from flask import Flask
import notify
from time import sleep
app = Flask(__name__)



'''
@app.route('/')
def mail():
    notify
    return 'sent'
'''

while(True):
    notify
    sleep(1)
    


if __name__ == '__main__':
    app.run()
