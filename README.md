# Flask основы

## API - GET запросы

Сумма чисел

```
http://localhost:5000/summa/?a=12&b=5
```

Произведение чисел

```
http://localhost:5000/proizved/?x=12&y=4
```

Добавление элемента в массив

```
http://localhost:5000/push/?v=george
```

Получение всех элементов массива

```
http://localhost:5000/all/
```

Получить все элементы массива в формате JSON

```
http://localhost:5000/get/json/all/
```

## API - POST запросы

Получить сумму чисел

```
curl -H "Content-Type: application/json" -d '{"a":10,"b":17}' -vv http://localhost:5000/post/json/summa/
```

## Docker

Создание и запуск контейнера

```
docker build -t python-flask-and-nginx-app .
docker images
docker run -p 80:5005 -ti d069f9cbcc36
```

Отправляем запросы

```
http://localhost/all/
http://localhost/push/?v=maxim
http://localhost/push/?v=nina
http://localhost/push/?v=george
http://localhost/all/
```

