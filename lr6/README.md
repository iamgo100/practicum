# Лабораторная работа №6

В данной лабораторной работе представлено выполненное задание - микросервис, который умеет:

* считать площадь параллелограмма и записывать результат вычислений;
* выдавать определенный существующий рассчет;
* обновлять определенный существующий рассчет;
* удалять определенный существующий рассчет.

```python
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
```

[Полный код микросервиса](https://github.com/iamgo100/practicum/blob/376eb373c3af3f6b4359a29b996f5adbcc3768d7/lr6/microservice.py)