from flask import Flask
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ffcbb1af81d63144389a5d6e'

@app.route('/')
def main():
    return json.loads('{"result" : "hello world"}')

@app.route('/hello_world', methods=('GET','POST'))
def hello():
    res = {}
    res.update({"success" : "true"})
    res.update({"result" : "hello world"})
    res.update({"version" : "1.0"})
    res = json.dumps(res)
    return json.loads(res)

if __name__ == "__main__":
    app.run(
        host='localhost', 
        port=9999
    )