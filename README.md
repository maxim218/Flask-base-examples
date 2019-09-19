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

## API - POST запросы

Получить сумму чисел

```
curl -H "Content-Type: application/json" -d '{"a":10,"b":17}' -vv http://localhost:5000/post/json/summa/
```

