# coding:utf-8
import os
from . import app, db
from todo.models import TODO, USER
from flask import session, render_template, \
    request, redirect, url_for, jsonify

basedir = os.path.abspath(os.path.join(__file__))


'''
@app.before_first_request
def init():
    db.create_all()
    chen = USER(name='chencheng', password='050400')
    db.session.add(chen)
    db.session.commit()
'''


@app.route('/')
def index():
    user = session.get('user', '')
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET'])
def login():
    user = session.get('user', '')
    return render_template('login.html', user=user)


@app.route('/resgiter', methods=['GET'])
def resgiter():
    return render_template('resgiter.html', user='')


@app.route('/todo', methods=['GET'])
def todo():
    user = session.get('user', '')
    todo_list = TODO.get_todo(user)

    return render_template('todo.html', user=user, todo_list=todo_list)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        user = session['user']
        todo = request.form.get('todo', '')
        describe = request.form.get('describe', '')
        if todo and describe:
            new_todo = TODO(todo=todo, user=user, description=describe)
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('todo'))
        else:
            return redirect(url_for('add_todo'))


@app.route('/done_todo', methods=['GET'])
def done_todo():
    user = request.args.get('user')
    todo_id = request.args.get('id')

    done_todo = TODO.query.filter_by(id=todo_id, user=user).first()
    db.session.delete(done_todo)
    db.session.commit()

    return redirect(url_for('todo'))


@app.route('/login_out', methods=['GET'])
def login_out():
    session['user'] = None
    return redirect(url_for('index'))


@app.route('/check_login', methods=['POST'])
def check_login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        data = USER.check_login(user, password)
        if data['msg'] == 'ok':
            session['user'] = user
        return jsonify(data)
    return redirect(url_for('login'))


@app.route('/check_resgiter', methods=['POST'])
def check_resgiter():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        msg = USER.resgiter(user, password)
        data = {'msg': ''}
        if msg == 'resgitered':
            data['msg'] = 'you already resgitered!'
        else:
            db.session.add(msg)
            db.session.commit()
            data['msg'] = 'ok'

        return jsonify(data)
    return redirect(url_for('resgiter'))


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(405)
def method_not_allow(e):
    return render_template('405.html'), 405


if __name__ == '__main__':
    app.run()
