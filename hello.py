from flask import Flask
from notify import notify
import time
app = Flask(__name__)



'''
@app.route('/')
def mail():
    notify
    return 'sent'
'''
while(True):
    notify("")
    time.sleep(20)
    


if __name__ == '__main__':
    app.run()
