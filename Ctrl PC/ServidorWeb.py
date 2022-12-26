from flask import Flask
from pynput.keyboard import Key, Controller

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/a')
def a():
    keyboard = Controller()
    keyboard.press("a")
    keyboard.release("a")
    return "hola"

if __name__ == '__main__':
   app.run( host='10.34.13.94' )