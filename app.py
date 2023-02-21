import oshttps://github.com/manupalhu/pyejer/blob/master/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Hola makina' 

@app.route('/how are you')
def hello():
    return 'Vamos tirando'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
