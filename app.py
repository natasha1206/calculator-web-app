"""
Calculator Web App (Backend with Flask)
--------------------------------------
This file runs the Flask server, serves the frontend (HTML/CSS/JS),
and provides a `/calculate` API endpoint to evaluate math expressions.
"""

import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Allowed math functions
        allowed = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,    # base-10 log
            "ln": math.log,       # natural log
            "factorial": math.factorial,
            "pi": math.pi,
            "e": math.e,
            "pow": pow
        }
        result = str(eval(expression, {"__builtins__": None}, allowed))
    except Exception:
        result = "Error"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)


