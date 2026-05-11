# Модель: Метод золотого перерізу (5 семестр)
# Автор: Іщенко Дмитро, група АІ-232

import math
from flask import Flask, request, jsonify

app = Flask(__name__)

def golden_section_search(f, a, b, epsilon=1e-4):
    phi = (1 + math.sqrt(5)) / 2
    resphi = 2 - phi

    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1 = f(x1)
    f2 = f(x2)

    iterations = 0
    while abs(b - a) > epsilon:
        iterations += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = f(x2)

    x_opt = (a + b) / 2
    return x_opt, f(x_opt), iterations

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        a = float(request.args.get('a', 0.5))
        b = float(request.args.get('b', 2.0))

        if a >= b:
            return jsonify({"error": "a must be less than b"}), 400

        def f(x):
            return x + 2 / x

        x_min, f_min, iters = golden_section_search(f, a, b)

        return jsonify({
            "model": "Метод золотого перерізу",
            "author": "Іщенко Дмитро, АІ-232",
            "input": {"a": a, "b": b},
            "result": {
                "x_min": round(x_min, 6),
                "f_min": round(f_min, 6),
                "iterations": iters
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "service": "Golden Section Search API",
        "author": "Іщенко Дмитро, АІ-232",
        "endpoint": "/calculate?a=0.5&b=2.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
