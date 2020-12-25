from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("main.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/reference')
def reference():
    return render_template("reference.html")


@app.route('/calculation')
def calculation():
    return render_template("calculation.html")


@app.route('/SO2')
def calcSO2():
    return render_template("SO2.html")


@app.route('/calc-heavy')
def calcHeavy():
    return render_template("/heavy-parts.html")


@app.route('/NOx')
def calcNOx():
    return render_template("NOx.html")


@app.route('/CO')
def calcCO():
    return render_template("CO.html")


@app.route('/CO2')
def calcCO2():
    return render_template("CO2.html")


@app.route('/N2O')
def calcN2O():
    return render_template("N2O.html")



if __name__ == '__main__':
    app.run(port=9998, debug=True)
