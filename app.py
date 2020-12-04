from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECERT_KEY'] = 'secretkey'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')
def messageReceived(methods=['GET', 'POST']):
    print('message received!')


@socketio.on('custom event')
def my_custom_event (json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
'''
@socketio.on('message')
def receive_message(message):
    print('######## : {}'.format(message))
    send('This is the message from Flask')


@socketio.on('custom event')
def receive_custom_event(json, methods=['GET', 'POST']):
    print('THE CUSTOM MESSAGE IS: {}'.format(json['name']))
    emit('from flask', {'extension': 'Flask-SocketIO'}, json=True)
'''

if __name__ == '__main__':
    # app.run()
    socketio.run(app, debug=True)
