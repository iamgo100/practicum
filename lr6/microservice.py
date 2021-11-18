from flask import Flask, request
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
    return json.dumps(res)

def read_json():
    with open('data.json') as data:
        file = json.load(data)
        return file, len(file)

def write_to_file(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

@app.route('/add_calc', methods=['POST'])
def calculate_square():
    data, length = read_json()
    id = length + 1
    a = float(request.form.get('a'))
    h = float(request.form.get('h'))
    if a and h:
        s = a*h
        data.append({"result" : s, "id" : id})
        write_to_file(data)
        return json.dumps({'success' : "true", 'result': s})
    return json.dumps({'success' : "false", 'result': "Неверно переданы аргументы"})

@app.route('/get_calc', methods=['POST'])
def get_square():
    data, _ = read_json()
    id = int(request.form.get('id'))
    if id:
        for calc in data:
            if int(calc['id']) == id:
                return json.dumps(calc)
        return json.dumps({'success' : "false"})
    return json.dumps({'success' : "false"})

@app.route('/update_calc', methods=['POST'])
def update_square():
    data, _ = read_json()
    id = int(request.form.get('id'))
    if id:
        for calc in data:
            if int(calc['id']) == id:
                a = float(request.form.get('a'))
                h = float(request.form.get('h'))
                if a and h:
                    s = a*h
                    calc.update({"result" : s})
                    write_to_file(data)
                    return json.dumps({'success' : "true"})
                return json.dumps({'success' : "false", 'result': "Неверно переданы аргументы"})
        return json.dumps({'success' : "false"})
    return json.dumps({'success' : "false"})

@app.route('/delete_calc', methods=['POST'])
def delete_square():
    data, _ = read_json()
    id = int(request.form.get('id'))
    if id:
        for calc in data:
            if int(calc['id']) == id:
                data.remove(calc)
                write_to_file(data)
                return json.dumps({'success' : "true"})
        return json.dumps({'success' : "false"})
    return json.dumps({'success' : "false"})

if __name__ == "__main__":
    app.run(
        host='localhost', 
        port=9999
    )