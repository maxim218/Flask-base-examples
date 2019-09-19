from flask import Flask, request, make_response

app = Flask(__name__)

def resultObject(s):
    s = str(s)
    resp = make_response(s)
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Connection"] = "close"
    resp.headers["Author"] = "Maxim" 
    return resp

@app.route('/summa/')
def summa():
    a = request.args.get('a')
    b = request.args.get('b')
    a = int(a)
    b = int(b)
    s = a + b
    return resultObject(s)

@app.route('/proizved/')
def proizved():
    x = request.args.get('x')
    y = request.args.get('y')
    x = int(x)
    y = int(y)
    p = x * y
    return resultObject(p)

arr = []

@app.route('/push/')
def push():
    v = request.args.get('v')
    v = str(v)
    arr.append(v)
    n = len(arr)
    s = "Size: " + str(n)
    return resultObject(s)

@app.route('/all/')
def all():
    s = ""
    for i in range(0, len(arr)):
        element = arr[i]
        s = s + " " + str(element)
    s = "Elements:" + s
    return resultObject(s)

if __name__ == '__main__':
    app.run()

