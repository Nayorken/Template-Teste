from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


def herokudb():
    Host = 'ec2-54-228-207-163.eu-west-1.compute.amazonaws.com'
    Database = 'd7ii2b8cn5pjkq'
    User = 'jgosyygzlirujs'
    Password = '4d6f7ae9fc7c83cc3848273939541475d5d1c585eb915f82231dbd418d5ba628'
    return psycopg2.connect(host=Host, database=Database, user=User, password=Password)


def gravar(v1, v2):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS usr (usr text, pwd text)")
    db.execute("INSERT INTO usr VALUES ( %s, %s)", (v1, v2))
    ficheiro.commit()
    ficheiro.close()
    return


def alterar(v1, v2):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("UPDATE usr SET pwd = %s WHERE usr = %s", (v2, v1))
    ficheiro.commit()
    ficheiro.close()
    return


def existe(v1):
    try:
        ficheiro = herokudb()
        db = ficheiro.cursor()
        db.execute("SELECT * FROM usr WHERE usr = %s", (v1,))
        valor = db.fetchone()
        ficheiro.close()
    except:
        valor = None
    return valor


def eliminar(v1):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("DELETE FROM usr WHERE usr = %s", (v1,))
    ficheiro.commit()
    ficheiro.close()
    return


def log(v1, v2):
    ficheiro = herokudb()
    db = ficheiro.cursor()
    db.execute("SELECT * FROM usr WHERE usr = %s and pwd = %s", (v1, v2,))
    valor = db.fetchone()
    ficheiro.close()
    return valor


@app.route('/newpass', methods=['POST', 'GET'])
def newpass():
    erro = None
    if request.method == "POST":
        v1 = request.form['usr']
        v2 = request.form['pwd']
        v3 = request.form['cpwd']
        if not existe(v1):
            erro = 'O Utilizador não existe.'
        elif v2 != v3:
            erro = 'A palavra passe não coincide.'
        else:
            alterar(v1, v2)
            erro = 'A palavra passe foi alterada.'
    return render_template('newpass.html', erro=erro)


@app.route('/registo', methods=['POST', 'GET'])
def registo():
    erro = None
    if request.method == "POST":
        v1 = request.form['usr']
        v2 = request.form['pwd']
        v3 = request.form['cpwd']
        if existe(v1):
            erro = 'O Utilizador já existe.'
        elif v2 != v3:
            erro = 'A palavra passe não coincide.'
        else:
            gravar(v1, v2)
            erro = 'Utilizador registado com Sucesso.'
    return render_template('registo.html', erro=erro)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    erro = None
    if request.method == "POST":
        v1 = request.form['usr']
        v2 = request.form['pwd']
        if not existe(v1):
            erro = 'O Utilizador não existe.'
        elif not log(v1, v2):
            erro = 'A senha está incorreta.'
        else:
            erro = 'Bem-vindo.'
    return render_template('login.html', erro=erro)


@app.route('/apagar', methods=['POST', 'GET'])
def apagar():
    erro = None
    if request.method == "POST":
        v1 = request.form['usr']
        v2 = request.form['pwd']
        if not existe(v1):
            erro = 'O Utilizador não existe.'
        elif not log(v1, v2):
            erro = 'A senha está incorreta.'
        else:
            eliminar(v1)
            erro = 'Conta eliminada com Sucesso.'
    return render_template('apagar.html', erro=erro)

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
    app.run(debug=True)
