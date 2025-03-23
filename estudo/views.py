from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Duduznx'
    idade = 19

    context = {
        'usuario' : usuario,
        'idade' : idade

    }
    return render_template('index.html', context=context)

@app.route('/nova/')
def novapagi():
    return 'Outra View'