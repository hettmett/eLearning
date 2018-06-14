from functools import wraps
from flask import session, flash, redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user']['id']:
            return func(*args, **kwargs)
        flash('Please Login !')
        return redirect(url_for('auth.login'))
    return wrapper


def role_required(*roles):
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if session.get('user', {}).get('role') in roles:
                return func(*args, **kwargs)
            flash('You do not have permission to access this page !')
            return redirect(url_for('auth.index'))
        return wrapped
    return wrapper
