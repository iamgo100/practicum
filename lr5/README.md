# Лабораторная работа №5

В данной лабораторной работе представлено выполненное задание: микросервис, который умеет считать площадь параллелограмма.

```python
@app.route('/get_square', methods=['POST'])
def calculate_square():
    a = float(request.form.get('a'))
    h = float(request.form.get('h'))
    if a and h:
        s = a*h
    else:
        s = "Неверно переданы аргументы"
    res = {}
    res.update({"success" : "true"})
    res.update({"result" : s})
    res.update({"version" : "1.0"})
    res = json.dumps(res)
    return json.loads(res)
```

[Полный код микросервиса](https://github.com/iamgo100/practicum/blob/12e188b91a13fb21514e4630e2987ea85f5139e7/lr5/microservice.py)