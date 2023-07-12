from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import Usuarios


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', usuarios = Usuarios.get_all() )


@app.route('/user/new')
def new():
    return render_template('new_user.html')

@app.route('/user/create', methods=['POST'])
def create():
    Usuarios.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit( id ):
    data ={ 
        "id": id
    }
    return render_template('edit_user.html', usuario = Usuarios.get_one(data) )

@app.route('/user/show/<int:id>')
def show( id ):
    data ={ 
        "id":id
    }
    usuario = Usuarios.get_one(data)
    if usuario:
        return render_template('show_user.html', usuario = usuario)
    else:
        return render_template('error.html', message='User not found')


@app.route('/user/update',methods=['POST'])
def update():
    Usuarios.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy( id ):
    data ={
        "id": id
    }
    Usuarios.destroy(data)
    return redirect('/users')