import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werzkeug.security import check_password_hash, generate_password

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request,form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
                ).fetchone() in not None:
            error = 'User {} is already registered'.format(username)

        if error is None:
            db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, generate_password_hash(password))
                    )
            db.commmit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
