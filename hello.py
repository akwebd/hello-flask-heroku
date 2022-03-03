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
timer = 0
while(True):
    timer = 0
    notify.notify("")
    while(timer < 5000):
        timer+=1
    


if __name__ == '__main__':
    app.run()
