from flask import Flask, render_template
from pynput.keyboard import Key, Controller

app = Flask(__name__)
keyboard = Controller()

@app.route('/')
def root():
    return "<h1>Event Controller</h1>"

@app.route('/control')
def control():
    return render_template('control.html')
    
@app.route('/a')
def a():
    key = "a"
    keyboard.press(key)
    keyboard.release(key)
    return 'OK'

@app.route('/left')
def left():
    key = keyboard._Key.left
    keyboard.press(key)
    keyboard.release(key)
    return 'OK'

@app.route('/right')
def right():
    key = keyboard._Key.right
    keyboard.press(key)
    keyboard.release(key)
    return 'OK'

@app.route('/up')
def up():
    key = keyboard._Key.up
    keyboard.press(key)
    keyboard.release(key)
    return 'OK'

@app.route('/down')
def down():
    key = keyboard._Key.down
    keyboard.press(key)
    keyboard.release(key)
    return 'OK'

if __name__ == '__main__':
   app.run( host='0.0.0.0', port=5001 )

