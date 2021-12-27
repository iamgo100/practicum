# Лабораторная работа №4

В данной лабораторной работе представлено выполненное задание: создание микросервиса с двумя эндпоинтами.

```python
@app.route('/hello_world', methods=('GET','POST'))
def hello():
    res = {}
    res.update({"success" : "true"})
    res.update({"result" : "hello world"})
    res.update({"version" : "1.0"})
    res = json.dumps(res)
    return json.loads(res)
```

[Полный код микросервиса](https://github.com/iamgo100/practicum/blob/12e188b91a13fb21514e4630e2987ea85f5139e7/lr4/microservice.py)