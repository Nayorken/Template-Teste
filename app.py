from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/p1')
def p1 ():
    return render_template('p1.html')

@app.route('/p2')
def p2 ():
    return render_template('p2.html')
@app.route('/p3')
def p3 ():
    return render_template('p3.html')

@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/registo')
def registo ():
    return render_template('registo.html')

@app.route('/categorias')
def categorias ():
    return render_template('categorias.html')

@app.route('/bebe')
def bebe ():
    return render_template('bebe.html')

@app.route('/lazer')
def lazer ():
    return render_template('lazer.html')

@app.route('/telemoveis')
def telemoveis ():
    return render_template('telemoveis.html')

@app.route('/agricultura')
def agricultura ():
    return render_template('agricultura.html')

@app.route('/animais')
def animais ():
    return render_template('animais.html')

@app.route('/desporto')
def desporto ():
    return render_template('desporto.html')

@app.route('/moda')
def moda ():
    return render_template('moda.html')

@app.route('/moveis')
def moveis ():
    return render_template('moveis.html')

@app.route('/tecnologia')
def tecnologia ():
    return render_template('tecnologia.html')

@app.route('/carros')
def carros ():
    return render_template('carros.html')

@app.route('/imoveis')
def imoveis ():
    return render_template('imoveis.html')

@app.route('/emprego')
def emprego ():
    return render_template('emprego.html')

@app.route('/serviços')
def serviços ():
    return render_template('serviços.html')

@app.route('/equipamento')
def equipamento ():
    return render_template('equipamento.html')

@app.route('/outras')
def outras ():
    return render_template('outras.html')

@app.route('/chill')
def chill ():
    return render_template('chill.html')

@app.route('/sobre')
def sobre ():
    return render_template('sobre.html')
if __name__ == '__main__':
    app.run(debug = True)
